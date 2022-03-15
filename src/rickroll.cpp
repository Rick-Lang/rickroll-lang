#include <iostream>
#include "lexer.h"

using namespace std;

int main(int argc, char *argv[]){
    cout<<readFile(argv[1])<<endl;
}