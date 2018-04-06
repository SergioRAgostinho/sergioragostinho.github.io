/**
  * \author Sérgio Agostinho - sergio(dot)r(dot)agostinho(at)gmail(dot)com
  * \date created: 2018/03/12
  */

function readTextFile(file, callback, args) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/text");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText, args);
        }
    }
    rawFile.send(null);
}

function writeReferences(text, args)
{
  // parse bibtex to a js object
  entries = bibtexParse.toJSON(text);

  // Flatten the object structure
  data = [];
  for (var i = 0; i < entries.length; ++i) {
    data.push(entries[i].entryTags);
  }

  fields = ["Author", "Title", "Year", "Publisher"];

  // Define my parsers
  function parse_title(title) {
    return document.createTextNode(title);
  }

  function parse_author(author) {
    authors = author.split(" and ");

    var names = [];
    for (var i = 0; i < authors.length; ++i) {
      var idx = authors[i].indexOf(",");
      if(idx > -1)
        names.push(authors[i].slice(0, idx).trim());
      else
      {
        var ns = authors[i].trim().split(" ");
        names.push(ns[ns.length - 1]);
      }
    }

    var string = "";
    if(names.length == 1)
      string = names[0];
    else if(names.length == 2)
      string = names[0] + " and " + names[1];
    else if(names.length > 2)
      string = names[0] + " et al.";

    return document.createTextNode(string);
  }

  function parse_year(year) {
    return document.createTextNode(year);
  }

  function parse_publisher(publisher) {
    if(!publisher)
      publisher = "";
    return document.createTextNode(publisher);
  }

  var parser = {
    "Author" : parse_author,
    "Title" : parse_title,
    "Year" : parse_year,
    "Publisher" : parse_publisher
  }

  // Sort data by authors last name
  // TODO. Parse last name only once
  data.sort(function(a,b) {
    if(parse_author(a["Author"]) < parse_author(b["Author"])) return -1;
    if(parse_author(a["Author"]) > parse_author(b["Author"])) return 1;
    return 0;
  });

  // Figure out pagination
  var page_size = args["page_size"];
  var page_count = Math.ceil(data.length / page_size);
  var parent = document.getElementById("references").parentElement;

  for (var i = 0; i < page_count; ++i) {
    var min = page_size * i;
    var max = Math.min(data.length, min + page_size);
    var table = createTableWithData(data.slice(min, max), fields, parser);

    // Find the right slide
    var slide = document.createElement("section");
    slide.appendChild(table);
    parent.appendChild(slide);
  }
}

function writeImageAttributions(text, args)
{
  var data = JSON.parse(text);

  var fields = ['id', 'author', 'url'];

  // Sort my elements by id
  data.sort(function(a,b) {
    if(a['id'] < b['id']) return -1;
    if(a['id'] > b['id']) return 1;
    return 0;
  });

  function parse_url(url) {
    if(!url)
      return document.createTextNode("");

    var a = document.createElement("a");
    a.setAttribute("href", url);
    a.appendChild(document.createTextNode("link"));
    return a
  }

  function parse_id(id) {
    return document.createTextNode(id);
  }

  function parse_author(author) {
    if(!(author instanceof Array))
      return document.createTextNode(author);

    if(author.length >= 3)
      return document.createTextNode(author[0] + " et. al");

    if(author.length == 2)
      return document.createTextNode(author[0] + "and" + author[1]);

    if(author.length == 1)
      return document.createTextNode(author[0]);
  }

  var parser = {
    "id": parse_id,
    "author": parse_author,
    "url" : parse_url
  };

  var page_size = args["page_size"];
  var page_count = Math.ceil(data.length / page_size);
  var parent = document.getElementById("attributions").parentElement;

  for (var i = 0; i < page_count; ++i) {
    var min = page_size * i;
    var max = Math.min(data.length, min + page_size);
    var table = createTableWithData(data.slice(min, max), fields, parser);

    // Find the right slide
    var slide = document.createElement("section");
    slide.appendChild(table);
    parent.appendChild(slide);
  }
}


function createTableWithData(data, fields, parser) {
  // Set up my table
  var table = document.createElement("table");
  var thead = document.createElement("thead");
  var tr_head = document.createElement("tr");

  // Build my header entries
  for (var i = 0; i < fields.length; ++i) {
    var th = document.createElement("th");
    var field_upper = fields[i].charAt(0).toUpperCase()
              + fields[i].slice(1);
    th.appendChild(document.createTextNode(field_upper));
    tr_head.appendChild(th);
  }
  thead.appendChild(tr_head);

  // The table body
  var tbody = document.createElement("tbody");

  // Construct the table body
  for (var i = 0; i < data.length; ++i) {
    var tr = document.createElement("tr");
    for (var j = 0; j < fields.length; ++j) {
      var td = document.createElement("td");
      td.appendChild(parser[fields[j]](data[i][fields[j]]));
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
  }

  table.appendChild(thead);
  table.appendChild(tbody);

  return table;
}