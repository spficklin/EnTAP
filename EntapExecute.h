//
// Created by harta on 3/4/17.
//

#ifndef ENTAP_ENTAPEXECUTE_H
#define ENTAP_ENTAPEXECUTE_H


#include "QuerySequence.h"
#include <list>
#include <boost/program_options/variables_map.hpp>

namespace entapExecute {
    std::list<std::string> verify_databases(std::vector<std::string>, std::vector<std::string>,
                                            std::vector<std::string>);
    void execute_main(boost::program_options::variables_map&);
    std::string genemarkST(std::string);
    std::string rsem(std::string, std::string, bool, int);
    std::string filter_transcriptome(std::string&, std::string&,float,std::string);
    void diamond_run(std::list<std::string>, std::string, int&);
    void diamond_parse(std::list<std::string>, std::string);
    void diamond_blast(std::string ,std::string, std::string,int&);
    bool is_contaminant(std::string,std::unordered_map<std::string, std::string>&);
    void print_map(std::unordered_map<std::string, QuerySequence>&);
    void verify_state(std::string&);
    bool is_file_empty(std::string);
    std::unordered_map<std::string, std::string> read_tax_map();

};


#endif //ENTAP_ENTAPEXECUTE_H
