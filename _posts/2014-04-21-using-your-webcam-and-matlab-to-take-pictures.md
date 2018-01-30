---
title: Using your webcam and MATLAB to take pictures
location: Lisbon, Portugal
excerpt: I've been messing around with some topics which had me implement some intermediate tools in MATLAB that might just be useful to some of you. Sharing is caring.
date: 2014-04-21 19:24
tags: [matlab]
# categories: [tutorials]
---

Hey all,

I've been messing around with some topics which had me implement some intermediate tools in MATLAB that might just be useful to some of you. Sharing is caring.

## Using your webcam and MATLAB to take pictures

For this example  you'll need the Image Acquisition Toolbox and Image Processing Toolbox (the latter only for color space conversion operations). I needed to have a quick way to take pictures from the video feed, so after a couples of minutes fooling around the internet, copying snippets here and there it resulted in

```matlab
%% Snapshot Acquisition

%data
buffer = {};

%Video acquisition
vInput = videoinput('winvideo',1);
set(vInput,'FramesPerTrigger',1);

% Create a customized GUI.
fHandle = figure('Name', 'Snapshot Taker');
set(fHandle,'WindowButtonDownFcn','buffer = store_image(vInput,buffer);');
uicontrol('String', 'Close', 'Callback', 'close(gcf);delete(vInput)');

% Create an image object for previewing.
vidRes = get(vInput, 'VideoResolution');
nBands = get(vInput, 'NumberOfBands');
hImage = image( zeros(vidRes(2), vidRes(1), nBands) );
preview(vInput, hImage);
```

In this example, I invoke ```videoinput('winvideo',1)``` because my webcam happened to be device number 1 connected to ```winvideo``` adapter. This will likely be the rule for most of us, but in case you're unaware of which adapter should you use, run ```imaqhwinfo``` to get more information on all the adapters available to your system. Use then ```imaqhwinfo(<your_adpator_name>)``` to check if there are available devices on it. 
Note that there is a ```store_image``` function which is called every time the mouse button is pressed on top of the video feed figure.

```matlab
function buffer = store_image(vidObject, buffer)

    frame = getsnapshot(vidObject);
    
    %change color space
    frameRgb = ycbcr2rgb(frame);
    
    figure;
    image(frameRgb);
    buffer = [buffer;{frameRgb}];
end
```

This function receives the video object and the cell array with previously taken pictures, and returns the latter with a new picture appended. It opens a new figure with each snapshot taken. 
When you are satisfied, you may want to save each image to an individual file. To do that run the following snippet

```matlab
%Dump buffer as files
for n= 1:numel(buffer)
    I = rgb2gray(buffer{n});
    imwrite(I,['calibration_data/image_',num2str(n),'.tif'],'tif');

end
```

Notice that in the end I actually store my images in grayscale, so simply remove the line invoking ```rbg2gray``` in case you want colored pictures. Finally, here's a screenshot on how things should like on your screen if everything went as expected.

![](/assets/images/posts/sstaker.jpg)