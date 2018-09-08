/**
  * \copyright 2018 HipsterTech
  * \copyright 2018 PaperMint Designs
  * \author Sergio Agostinho - sergio(dot)r(dot)agostinho(at)gmail(dot)com
  * \date created: 2018/04/11
  * \file timer_tester.cpp
  */
#include <condition_variable>
#include <thread>
#include <mutex>
#include <iostream>
#include <chrono>
#include <queue>
#include <vector>

void
p1s ()
{
  std::cout << "1s." << std::endl;
}

void
p2s ()
{
  std::cout << "2s." << std::endl;
}

void
p3s ()
{
  std::cout << "3s." << std::endl;
}

void
p4s ()
{
  std::cout << "5ms." << std::endl;
}

void
p5s ()
{
  std::cout << "10ms." << std::endl;
}

typedef std::pair<std::chrono::high_resolution_clock::time_point, void (*)(void)> T;
struct less
{
  bool operator() (const T& lhs, const T& rhs)
  {
    return lhs.first > rhs.first;
  }
};

int
main ()
{

  // std::thread t (print);
  std::mutex mutex;
  std::condition_variable cv;

  typedef std::chrono::high_resolution_clock std_clock;
  std_clock::time_point now = std_clock::now ();
  std_clock::time_point t3 = now + std::chrono::seconds (3);
  std_clock::time_point t2 = now + std::chrono::seconds (2);
  std_clock::time_point t1 = now + std::chrono::seconds (1);
  std_clock::time_point t4 = now + std::chrono::milliseconds (5);
  std_clock::time_point t5 = now + std::chrono::milliseconds (10);

  std::priority_queue<T, std::vector<T>, less> q;
  q.emplace (t3, &p3s);
  q.emplace (t2, &p2s);
  q.emplace (t1, &p1s);
  q.emplace (t4, &p4s);
  q.emplace (t5, &p5s);

  std::unique_lock<std::mutex> lock (mutex);

  while (true)
  {
    std_clock::time_point t = q.top ().first;
    while (cv.wait_until (lock,t) == std::cv_status::no_timeout) {}

    (*q.top ().second)();
    q.pop ();
    if (q.empty ())
      break;
  }

  // t.join ();
  return 0;
}