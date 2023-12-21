#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <iostream>
#include <nlohmann/json.hpp>

using namespace std;
using Eigen::MatrixXd;
using Eigen::VectorXd;
using json = nlohmann::json;

class Task {
 public:
  float identifier;
  MatrixXd A;
  MatrixXd b;
  MatrixXd x;
  float time;

  Task() {
    // get the JSON information for the local url using the port 8000
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000"});
    // cout << r.text << endl; // print the cpr Response text

    // parse the text with json
    json data = json::parse(r.text);
    // cout << data << endl; // print the text parsed by json

    // get the id of the task
    identifier = data.at("id");

    // get the time
    time = data.at("time");

    // get the matrix A
    auto a_json = data.at("a");
    A = MatrixXd(a_json.size(), a_json[0].size());
    for (int i = 0; i < a_json.size(); i++) {
      for (int j = 0; j < a_json[0].size(); j++) {
        A(i, j) = a_json[i][j];
      }
    }

    // get the matrix b
    auto b_json = data.at("b");
    b = VectorXd(b_json.size());
    for (int i = 0; i < b_json.size(); i++) {
      b(i) = b_json[i];
    }

    // get the matrix x
    auto x_json = data.at("x");
    x = VectorXd(x_json.size());
    for (int i = 0; i < x_json.size(); i++) {
      x(i) = x_json[i];
    }

    // display the task
    // cout << identifier << "\n\n"
    //   << A << "\n\n" << b << "\n\n"
    //   << x << "\n\n" << time << endl;
  }

  void work(bool display_time) {
    auto start = chrono::high_resolution_clock::now();
    x = A.colPivHouseholderQr().solve(b);
    // x = A.lu().solve(b);
    auto stop = chrono::high_resolution_clock::now();
    if (display_time) {
      auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
      cout << "Time : " << duration.count() * 1e-6 << " seconds" << endl;
    }
  }
};

int main() {
  // to constrain the max number of thread used by Eigen
  // Eigen::setNbThreads(4);
  Task my_task = Task();
  my_task.work(true);  // execute the task
  return 0;
}

/*
#compile
$ cmake --build build
#execute
$ ./build/low_level
*/
