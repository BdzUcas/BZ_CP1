#BZ 1st For loops notes
import time as t
jingle_bells = ['dashing through the snow',1.5,'in a one horse open sleigh',1.5,'o\'re the hills we gooooooo',1.5,'laughing all the way',1.5,'bells on bobtails ring',1.5,'making spirits bright',1.5,'what fun it is',0.75, 'to ride and sing',0.75,'a sleighing song tonight',1,'OOOOOHHHHH',0.5,'Jingle bells',0.75,'jingle bells',0.75,'jingle all the waaaaay',1.5,'oh what fun',0.75,'it is to ride',0.75,'in a one horse open sleigh,',1,'hey!',0.5,'Jingle bells',0.75,'jingle bells',0.75,'jingle all the waaaaay',1.5,'oh what fun',0.75,'it is to ride',0.75,'in a one',1,'horse',1,'open',1,'sleeeeeiggghhhh!!!']
i = 1
for line in jingle_bells:
    if i % 2 == 1:
        print(line)
    else:
        t.sleep(line)
    i += 1

dracula = range(1,10)