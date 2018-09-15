#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:52:45 2018

@author: samyu
"""
# Header
header = ("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n"
          "<!DOCTYPE score-partwise PUBLIC\n"
          " \"-//Recordare//DTD MusicXML 3.1 Partwise//EN\"\n"
          " \"http://www.musicxml.org/dtds/partwise.dtd\">\n"
          "<score-partwise version=\"3.1\">\n"
          " <part-list>\n"
          " <score-part id=\"P1\">\n"
          " <part-name>Music</part-name>\n"
          " </score-part>\n"
          " </part-list>\n")

# Start/end part
start_part = "<part id=\"P1\">"
end_part = "</part>"

# Assume 4-4 time and C major key.
# TODO (if time): guess key/key signature
attributes = ("<attributes>\n"
              "<divisions>1</divisions>\n"
              "<key>\n"
              "<fifths>0</fifths>\n"
              "</key>\n"
              "<time>\n"
              "<beats>4</beats>\n"
              "<beat-type>4</beat-type>\n"
              "</time>\n"
              "<clef>\n"
              "<sign>G</sign>\n"
              "<line>2</line>\n"
              "</clef>\n"
              "</attributes>\n")

# Add notes
# Assume quarter notes (for now).
notes = [] # TODO: read in notes from Emily's output file.
for note in notes:
    