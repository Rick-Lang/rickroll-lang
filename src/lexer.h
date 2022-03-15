#pragma once
#include<string>
#include<fstream>
using namespace std;

string readFile(char *filename){
    fstream myfile;
    myfile.open(filename, ios::in);
    string result;
    string tp;
    while(getline(myfile, tp)){
        result = result + tp + "\n";
    }
    myfile.close();
    return result;
}