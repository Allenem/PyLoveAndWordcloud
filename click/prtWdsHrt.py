import time
words = input('Please input the words you want to say!:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y) % len(item)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(12, -12, -1)]))
    time.sleep(1.5)

# example: 
# input: I love U 
# output:
'''
                IIIIIIIII           IIIIIIIII
            IIIIIIIIIIIIIIIII   IIIIIIIIIIIIIIIII
          IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
         IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
         IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
          IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
          IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
            IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
             IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
              IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                IIIIIIIIIIIIIIIIIIIIIIIIIIIII
                  IIIIIIIIIIIIIIIIIIIIIIIII
                    IIIIIIIIIIIIIIIIIIIII
                       IIIIIIIIIIIIIII
                          IIIIIIIII
                             III
                              I

                velovelov           velovelov
            elovelovelovelove   elovelovelovelove
          velovelovelovelovelovelovelovelovelovelov
         velovelovelovelovelovelovelovelovelovelovel
        velovelovelovelovelovelovelovelovelovelovelov
        elovelovelovelovelovelovelovelovelovelovelove
        lovelovelovelovelovelovelovelovelovelovelovel
        ovelovelovelovelovelovelovelovelovelovelovelo
        velovelovelovelovelovelovelovelovelovelovelov
        elovelovelovelovelovelovelovelovelovelovelove
         ovelovelovelovelovelovelovelovelovelovelove
          elovelovelovelovelovelovelovelovelovelove
          lovelovelovelovelovelovelovelovelovelovel
            elovelovelovelovelovelovelovelovelove
             ovelovelovelovelovelovelovelovelove
              elovelovelovelovelovelovelovelove
                velovelovelovelovelovelovelov
                  ovelovelovelovelovelovelo
                    lovelovelovelovelovel
                       lovelovelovelov
                          lovelovel
                             lov
                              v

                UUUUUUUUU           UUUUUUUUU
            UUUUUUUUUUUUUUUUU   UUUUUUUUUUUUUUUUU
          UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
         UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
        UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
         UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
          UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
          UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
            UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
             UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
              UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
                UUUUUUUUUUUUUUUUUUUUUUUUUUUUU
                  UUUUUUUUUUUUUUUUUUUUUUUUU
                    UUUUUUUUUUUUUUUUUUUUU
                       UUUUUUUUUUUUUUU
                          UUUUUUUUU
                             UUU
                              U
'''