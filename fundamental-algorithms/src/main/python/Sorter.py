#!/usr/bin/env python
"""
    Copyright 2012 Denys Sobchyshak

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__author__ = "Denys Sobchyshak"
__email__ = "denys.sobchyshak@gmail.com"

class Sorter:
    """
        Provides implementation of basic sorting algorithms.
    """

    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(list2sort):
        for i in range(0, len(list2sort)-1):
            for j in range(len(list2sort)-1, 0, -1):
                if list2sort[j-1] > list2sort[j]:
                    list2sort[j-1], list2sort[j] = list2sort[j],list2sort[j-1]
        return list2sort

    def insertion_sort(self, list_to_sort):
        #TODO:implement
        pass

    def quick_sort(self, list_to_sort):
        #TODO:implement
        pass

if __name__ == '__main__' :
    pass
