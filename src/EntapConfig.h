/*
 * Developed by Alexander Hart
 * Plant Computational Genomics Lab
 * University of Connecticut
 *
 * For information, contact Alexander Hart at:
 *     entap.dev@gmail.com
 *
 * Copyright 2017-2018, Alexander Hart, Dr. Jill Wegrzyn
 *
 * This file is part of EnTAP.
 *
 * EnTAP is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * EnTAP is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with EnTAP.  If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef ENTAPCONFIG_H
#define ENTAPCONFIG_H

#include <boost/serialization/unordered_map.hpp>
#include <boost/program_options/variables_map.hpp>
#include "common.h"
#include "UserInput.h"

struct  GoEntry {
    std::string go_id;
    std::string level;
    std::string category;
    std::string term;
    friend class boost::serialization::access;
    template <typename Archive>
    void serialize(Archive & ar, const uint32 v) {
        ar&go_id;
        ar&level;
        ar&category;
        ar&term;
    }
    GoEntry() {
        go_id = "";
        level = "";
        category = "";
        term = "";
    }
};

struct TaxEntry {
    std::string tax_id;
    std::string lineage;
    std::string tax_name;
    friend class boost::serialization::access;
    template<typename Archive>
    void serialize(Archive & ar, const uint32 v) {
        ar&tax_id;
        ar&lineage;
    }
    bool is_empty() {
        return this->tax_id.empty() && this->lineage.empty();
    }
    TaxEntry() {
        tax_id = "";
        lineage = "";
        tax_name = "";
    }
};

namespace entapConfig {
    //****************** Global Prototype Functions******************
    void execute_main(UserInput*, FileSystem*);
}

#endif //ENTAP_INITHANDLER_H
