#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:52:45 2018

@author: samyu
"""
def make_music_xml(lyric_syllables):
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
    end_score_partwise = "</score-partwise>"
    
    # Start/end part
    start_part = "<part id=\"P1\">\n"
    end_part = "</part>\n"
    
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
    with open("/Users/samyu/Downloads/notesData.txt") as f:
        content = f.read()
        content = content[1:len(content) - 1]
        notes = content.split(",") 
    measures = {}
    measure_num = 0
    count = 0
    measure_length = 4
    # TODO: Add value for lyric
    for note in notes:
        if count % measure_length == 0:
            if measure_num in measures:
                measures[measure_num] += "</measure>\n"
            measure_num += 1
            measures[measure_num] = f"<measure number=\"{measure_num}\">\n"
        note_string = "<note>\n<pitch>\n"
        if len(note) == 1:
            note_string += "<step>" + note + "</step>\n" 
        elif len(note) == 2:
            note_string += "<step>" + note[0] + "</step>\n" 
            note_string += "<alter>" + note[1] + "</alter>\n" 
        else:
            print("error! note is " + note)
        # TODO: How to determine octave??
        note_string += f"<octave>4</octave>\n</pitch>\n"
        note_string += "<duration>1</duration>\n<type>quarter</type>\n</note>\n"
        if count < len(lyric_syllables):
            note_string += f"<lyric>\n<syllabic>{lyric_syllables[count][0]}</syllabic>\n"
            note_string += f"<text>{lyric_syllables[count][1]}</text>\n</lyric>\n"
        measures[measure_num] += note_string
        count += 1
    all_measures = [measures[k] for k in measures]
    all_measures_string = "".join(all_measures)
    # Assemble string
    xml_content = (header + start_part + attributes + all_measures_string
                   + "</measure>\n" + end_part + end_score_partwise)
    with open("/Users/samyu/Desktop/score.xml", "w") as f:
        f.write(xml_content)

# Temporary syllables list for testing purposes      
syllables = [('single', 'Let'), ('single', 'me'), ('single', 'tell'), ('single', 'you'), ('single', 'what'), ('single', 'I'), ('single', 'was'), ('single', 'when'), ('single', 'I'), ('single', 'was'), ('single', 'young'), ('single', 'You'), ('single', 'have'), ('single', 'no'), ('begin', 'con'), ('end', 'trol'), ('begin', 'prece'), ('end', 'dent'), ('begin', 'Jef'), ('middle', 'fer'), ('end', 'son'), ('single', "I'll"), ('single', 'give'), ('single', 'him'), ('single', 'this'), ('single', 'His'), ('begin', 'fi'), ('middle', 'nan'), ('end', 'cial'), ('begin', 'sys'), ('end', 'tem'), ('single', 'is'), ('single', 'a'), ('single', 'work'), ('single', 'of'), ('begin', 'ge'), ('end', 'nius'), ('single', 'I'), ('begin', 'could'), ('end', "n't"), ('begin', 'un'), ('end', 'do'), ('single', 'it'), ('single', 'if'), ('single', 'I'), ('single', 'try'), ('single', 'and'), ('single', "I've"), ('single', 'tried'), ('begin', 'Pres'), ('middle', 'i'), ('end', 'dent'), ('begin', 'Madi'), ('end', 'son'), ('single', 'He'), ('single', 'took'), ('single', 'our'), ('begin', 'coun'), ('end', 'try'), ('single', 'from'), ('begin', 'bank'), ('middle', 'rupt'), ('end', 'cy'), ('single', 'I'), ('single', 'hate'), ('single', 'to'), ('begin', 'ad'), ('end', 'mit'), ('single', 'it'), ('single', 'but'), ('single', 'he'), ('begin', 'does'), ('end', "n't"), ('single', 'get'), ('single', 'enough'), ('begin', 'cred'), ('end', 'it'), ('single', 'for'), ('single', 'all'), ('single', 'the'), ('begin', 'cred'), ('end', 'it'), ('single', 'he'), ('single', 'gave'), ('single', 'us'), ('single', 'three'), ('single', 'on'), ('single', 'their'), ('begin', 'found'), ('end', 'ing'), ('begin', 'Fa'), ('end', 'ther'), ('begin', 'sto'), ('end', 'ry'), ('single', 'gets'), ('single', 'told'), ('begin', 'Ev'), ('end', 'ery'), ('begin', 'oth'), ('end', 'er'), ('begin', 'found'), ('end', 'ing'), ('begin', 'fa'), ('end', 'ther'), ('single', 'gets'), ('single', 'to'), ('single', 'grow'), ('single', 'old'), ('single', 'He'), ('begin', 're'), ('middle', 'mem'), ('end', 'bers'), ('single', 'your'), ('single', 'name'), ('single', 'keeps'), ('single', 'your'), ('begin', 'wast'), ('end', 'ing'), ('single', 'time'), ('begin', 'on'), ('end', 'to'), ('single', 'my'), ('single', 'live'), ('begin', 'An'), ('middle', 'oth'), ('end', 'er'), ('single', '50'), ('single', 'years'), ('single', 'No'), ('begin', 'sol'), ('end', 'dier'), ('single', 'to'), ('single', 'make'), ('single', 'sense'), ('single', 'of'), ('begin', 'your'), ('end', 'self'), ('single', 'You'), ('begin', 're'), ('middle', 'al'), ('end', 'ly'), ('single', 'do'), ('single', 'well'), ('single', "She's"), ('single', 'tell'), ('single', 'you'), ('single', 'a'), ('begin', 'trin'), ('middle', 'i'), ('end', 'ty'), ('single', 'church'), ('single', 'When'), ('single', 'I'), ('begin', 'need'), ('end', 'ed'), ('single', 'it'), ('single', 'on'), ('single', 'time'), ('single', "I'm"), ('single', 'still'), ('single', 'not'), ('single', 'through'), ('single', 'his'), ('begin', 'kind'), ('end', 'ness'), ('single', 'He'), ('single', 'gives'), ('single', 'me'), ('single', 'what'), ('single', 'me'), ('single', 'my'), ('single', 'raise'), ('single', 'funds'), ('single', 'for'), ('single', 'the'), ('begin', 'Wash'), ('middle', 'ing'), ('end', 'ton'), ('single', 'and'), ('single', 'when'), ('single', 'my'), ('single', 'time'), ('single', 'have'), ('single', 'I'), ('single', 'done'), ('single', 'enough'), ('single', 'Can'), ('single', 'I'), ('single', 'show'), ('single', 'you'), ('single', 'what'), ('single', 'the'), ('single', 'first'), ('begin', 'pri'), ('end', 'vate'), ('begin', 'or'), ('middle', 'phan'), ('end', 'age'), ('begin', 'hun'), ('end', 'dreds'), ('single', 'Get'), ('single', 'to'), ('single', 'see'), ('single', 'them'), ('begin', 'grow'), ('end', 'ing'), ('single', 'I'), ('single', 'see'), ('begin', 'ev'), ('end', 'ery'), ('single', 'time'), ('single', 'Oh'), ('single', 'I'), ('single', "can't"), ('single', 'wait'), ('single', 'to'), ('single', 'see'), ('single', 'him'), ('single', 'You')]
make_music_xml(syllables)