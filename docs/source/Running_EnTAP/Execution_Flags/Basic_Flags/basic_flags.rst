Basic Usage Flags
=====================

These are just some basic/common flags to use during Execution. You'll see these repeated on the other pages. All these flags can only be used via the command line.

*-*-runP / *-*-runN [CMD]
------------------------------
* Specify a blastp or blastx annotation
* If - -runP is selected with a nucleotide input, frame selection will be ran and annotation stages will be executed with protein sequences (blastp)
* If - -runP is selected with a protein input, frame selection will not be ran and annotation will be executed with protein sequences (blastp)
* If - -runN is selected with nucleotide input, frame selection will not be ran and annotation will be executed with nucleotide sequences (blastx)

-i / *-*-input [string] [CMD]
----------------------------------
* Path to the transcriptome file (either nucleotide or protein)

-d / *-*-database [multi-string] [CMD]
--------------------------------------------
* Specify up to 5 DIAMOND configured databases you would like to search agianst

*-*-out-dir [string] [CMD]
---------------------------------
* Specify an output directory for all of the files generated by EnTAP
* Default: Current working directory

-t / *-*-threads [integer] [CMD]
-------------------------------------
* Specify thread count for execution

*-*-|flag_path| [string] [CMD]
-----------------------------------
* Point to |config_file| to specify file paths
* Default: |config_file| residing in the current working directory

*-*-version [CMD]
-------------------
    * Prints the current EnTAP version you are running

-a / *-*-align [string] [CMD]
--------------------------------
* Path to alignment file (either SAM or BAM format)
* **Note:** Ignoring this flag will skip expression filtering
* If you have ran alignment with single end reads be sure to use the - -single-end flag as well (paired-end is default)
* Be sure to specify an FPKM threshold