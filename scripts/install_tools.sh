#!/bin/bash
echo "Initializing Linux Environment for MTB Analysis..."
# Example of installing a public domain bio-tool
sudo apt-get update
sudo apt-get install -y samtools bwa fastqc
echo "Tools installed successfully. Pipeline ready."
