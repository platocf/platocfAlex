#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【教程】如何用Python中的chardet去检测字符编码类型
http://www.crifan.com/python_chardet_example_show_how_to_use_to_detect_charset

Version:    2013-09-16
Author:     Crifan Li
Contact:    http://www.crifan.com/contact_me/
"""

import chardet


def chardet_detect_str_encoding(inputStr):
    """
        Demo how to use chardet to detect string encoding/charset
    """
    detectedEncodingDict = chardet.detect(inputStr);
    #print "type(detectedEncodingDict)=", type(detectedEncodingDict);  # type(detectedEncodingDict)= <type 'dict'>
    #print "detectedEncodingDict=", detectedEncodingDict;  # detectedEncodingDict= {'confidence': 0.99, 'encoding': 'utf-8'}
    detectedEncoding = detectedEncodingDict['encoding'];
    #print "That is, we have %d%% confidence to say that the input string encoding is %s" % (
    #int(detectedEncodingDict['confidence'] * 100), detectedEncoding)
    return detectedEncoding


if __name__ == '__main__':
    inputStr = "当前文件时UTF-8，所以你所看到的这段字符串，也是UTF-8编码的";
    chardet_detect_str_encoding(inputStr);