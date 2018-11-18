#!/bin/sh

touch $1
NOW=$(date +%F)
echo '#! /home/cam/anaconda3/bin/python3' >> $1
echo '"""' >> $1
echo 'file:' $1 >> $1
echo 'Cameron Kimber' >> $1
echo 'date:' $NOW >> $1
echo 'Class: CSE107' >> $1
echo 'Assignment:' >> $1
echo '"""' >> $1
echo '' >> $1
echo '' >> $1
echo 'def main():' >> $1
echo '' >> $1
echo '' >> $1
echo 'if __name__ == "__main__":' >> $1
echo '' >> $1
echo '    main()' >> $1
echo $(chmod +x $1)
