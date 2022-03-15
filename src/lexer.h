#pragma once
#include "keywords.h"

vector<string> lex_stmt(string *stmt){
    string current_tok;
    int quote_count;
    vector<string> tokens;
    for(char ch : *stmt){
        if(ch == '"'){
            quote_count += 1;
        }
        if(ch == '#'){
            break;
        }

    }
    return tokens;
}

vector<string> lexicalize(char *filename){
    vector<string> tokens;
    fstream myfile;
    myfile.open(filename, ios::in);
    string stmt;
    while(getline(myfile, stmt)){
        tokens.push_back(lex_stmt(&stmt));
    }
    myfile.close();
}
