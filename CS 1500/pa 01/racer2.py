import math
#!/usr/bin/env ipython3
'''
taylor@mst.edu
'''

# Edit any part of this file. 
# Write more functions, if you like.
# We give you the map to be used, as a head-start on the coding, below.
def displayIntro():
    print('''
Welcome to ASCII-racer.
Navigate through to the light at the end of the tunnel to win!
Press 'a' for left,'d' for right, enter for nothing
If you hit the walls, you lose.
To win you have to complete 2 laps around the tunnel array.
Press any key to start!''')

def displayLight():
    print('    _------_')
    print('  -~        ~-')
    print(' -     _      -')
    print('-      |>      -')
    print('-      |<      -')
    print(' -     |>     -')
    print('  -    ||    -')
    print('   -   ||   -')
    print('    -__||__-')
    print('    |______|')
    print('    <______>')
    print('    <______>')
    print('       \/')
    print('\n')

def win_screen():
    print("\033[H\033[J")
    print()
    print("                                   .''.")
    print("       .''.      .        *''*    :_\\/_:     .")
    print("      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.")
    print("  .''.: /\\ :    /)\\   ':'* /\\ *  : '..'.  -=:o:=-")
    print(" :_\\/_:'.:::.  | ' *''*    * '.\\'/.'_\\(/_ '.':'.'")
    print(" : /\\ : :::::  =  *_\\/_*     -= o =- /)\\     '   ")
    print("  '..'  ':::' === * /\\ *     .'/.\\'.  ' ._____")
    print("      *        |   *..*         :       |.   |' .---\"|")
    print("        *      |     _           .--'|  ||   | _|    |")
    print("        *      |  .-'|       __  |   |  |    ||      |")
    print("     .-----.   |  |' |  ||  |  | |   |  |    ||      |")
    print(" ___'       ' /\"\\ |  '-.\"\".    '-'   '-.'    '`      |____")
    print("   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                       ~-~-~-~-~-~-~-~-~-~   /|")
    print("                 ~-~-~-~-~-~-~-~  /|~       /_|\\")
    print("        ~-~-~-  -~-~-~-~-~-~     /_|\\    -~======-~")
    print("~-~~~~~~~~~~~~~     ~-~-~-~     /__|_\\ ~-~-~-~")
    print("~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~")
    print("      ~-~~-~-~-~-~-~-~-~-~-~-~-~ ~-~~-~-~-~-~")
    print("                        ~-~~-~-~-~-~")
    print('                ')
    print('You win!')
    print()

def lose_screen():
    print(
        '''
     _.--"""""--._                                                                                                                    
   .'             '.                                                                                                                  
  /                 \                                                                                                                 
 ;                   ;                                                                                                                
 |                   |                                                                                                                
 |                   |                                                                                                                
 ;                   ;                                                                                                                
  \ (`'--,    ,--'`) /                                                                                                                
   \ \  _ )  ( _  / /                                                                                                                 
    ) )(')/  \(')( (                                                                                                                  
   (_ `""` /\ `""` _)                                                                                                                 
    \`"-, /  \ ,-"`/                                                                                                                  
     `\ / `""` \ /`                                                                                                                   
      |/\/\/\/\/\|                                                                                                                    
      |\        /|                                                                                                                    
      ; |/\/\/\| ;                                                                                                                    
       \`-`--`-`/                                                                                                                     
        \      /                                                                                                                      
         ',__,'                                                                                                                       
          q__p                                                                                                                        
          q__p                                                                                                                        
          q__p                                                                                                                        
          q__p                                                                                                                        
                                                                                                                                      
You hit the wall, and lose!
'''
    )
def insertCar(track, position):
    # Make the different parts of the single row
    firstPart = track[0:position]
    secondPart = track[position+1:]

    fullTrack = firstPart + '^' + secondPart
    return fullTrack

def badMove(org_track, potential):
    ''' 
    Where org_track is the original track
    Where potential is the theoretical index
    '''
    if not(org_track[potential] == ' '):
        return True
    else: 
        return False


def ascii_racer():
    # This is the "map" that needs to be completed twice to win.
    # I do not suggest modifying this map.
    my_lib = ['  |*     *|',
              '   |*     *|',
              '    |*     *|',
              '   |*      *|',
              '  |*      *|',
              ' |*      *|',
              ' |*      *|',
              '  |*     *|',
              '   |*     *|',
              '    |*     *|',
              '     |*     *|',
              '      |*     *|',
              '       |*     *|',
              '        |*     *|',
              '       |*     *|',
              '      |*     *|',
              '     |*     *|',
              '    |*     *|',
              '   |*     *|',
              '  |*     *|',
              ' |*     *|',
              '|*     *|',
              ' |*     *|']

    print('                            _.-="_-         _')
    print('                         .-="   _-          | ||"""""""---._______     __..')
    print('             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __')
    print('      __.--""     __        ,'                  ' o \           __ [__|')
    print(' __-""=======.--""  ""--.=================================.--""  ""--.=======:')
    print(']       [w] : /        \ : |========================|    : /        \ :  [w] :')
    print('V___________:|          |: |========================|    :|          |:   _-"')
    print(' V__________: \        / :_|=======================/_____: \        / :__-"')
    print(' -----------\' "-______-" -------------------------------'  '-____- ')

    displayIntro()

    answer = input()
    if answer == '' or not answer == '':
 
        length = len(my_lib)
        broken = False
        i = 0
        mutations = 0
        for n in range(0,20):
            mutate = (len(my_lib[n])/2) + mutations
            print('ASCII Racer 1.0, level: %d of 23 rows in lap number %d\n' % (i,1))
            displayLight()
            a = n
            b = a + 1
            c = n + 2
            if n == 0:
                print(my_lib[a])
                print(my_lib[b])
                mutate = math.ceil(len(my_lib[c]) / 2) + mutations
                mutate = int(mutate)
                print(insertCar(my_lib[c], mutate))
            elif n == 19:
                #print(my_lib[0])
                #print(my_lib[1])
                #print(my_lib[2])

                break
            elif n < 21:
                print(my_lib[a])
                print(my_lib[b])
                mutate = math.ceil(len(my_lib[c]) / 2) + mutations
                mutate = int(mutate)
                print(insertCar(my_lib[c],mutate))
                bad = badMove(my_lib[c], mutate)
                if bad:
                    broken = True
                    break
                else:
                    broken = False
            '''
            elif n == 21:
                print(my_lib[n])
                print(my_lib[n+1])
                mutate = math.ceil(len(my_lib[0]) / 2) + mutations
                mutate = int(mutate)
                print(insertCar(my_lib[0], mutate))
            elif n == 22:
                print(my_lib[n])
                print(my_lib[0])
                mutate = math.ceil(len(my_lib[1]) / 2) + mutations
                mutate = int(mutate)
                print(insertCar(my_lib[1],mutate))
            '''
            x =input()
            isOkay = (x == 'a' or x == 'd' or x == '')
            while not isOkay:
                x = input()
                isOkay = (x == 'a' or x == 'd' or x == '')
            if isOkay:
                if (x == 'a'):
                    # Move left
                    mutations = -1
                elif (x == 'd'):
                    # Move right
                    mutations = 1
                elif (x == ''):
                    # Move forward
                    mutations = 0

            print("\033[H\033[J")
            i = i + 1
        # This clears the screen, producing the wierd characters in ZyBooks, but makes it nice on your computer
        print("\033[H\033[J")

        i = 0
        mutations = 0
        win = False

        for n in range(0,length):
            if broken:
                break
            else:
                mutate = (len(my_lib[n])/2) + mutations
                print('ASCII Racer 1.0, level: %d of 23 rows in lap number %d\n' % (i,2))
                displayLight()
                    
                a = n
                b = a + 1
                c = a + 2
                if n == 0:
                    print(my_lib[a])
                    print(my_lib[b])
                    mutate = math.ceil(len(my_lib[c])/2) + mutations
                    mutate = int(mutate)
                    print(insertCar(my_lib[c],mutate))
                elif n < 21:
                    print(my_lib[a])
                    print(my_lib[b])
                    mutate = math.ceil(len(my_lib[c])/2) + mutations
                    mutate = int(mutate)
                    bad = badMove(my_lib[c], mutate)
                    if bad:
                        broken = True
                        break
                    else:
                        broken = False
                        print(insertCar(my_lib[c],mutate))
                    
                elif n == 21:
                    print(my_lib[n])
                    print(my_lib[n+1])
                    mutate = math.ceil(len(my_lib[0])/2) + mutations
                    mutate = int(mutate)
                    bad = badMove(my_lib[0], mutate)
                    if bad:
                        broken = True
                        break
                    else:
                        broken = False
                        print(insertCar(my_lib[0],mutate))
                elif n == 22:
                    print(my_lib[n])
                    print(my_lib[0])
                    mutate = math.ceil(len(my_lib[1])/2) + mutations
                    mutate = int(mutate)
                    bad = badMove(my_lib[1], mutate)
                    if bad:
                        broken = True
                        break
                    else:
                        broken = False
                        print(insertCar(my_lib[1],mutate))
                        win = True

                x = input()
                isOkay = (x == 'a' or x == 'd' or x == '')
                while not isOkay:
                    x = input()
                    isOkay = (x == 'a' or x == 'd' or x == '')
                if isOkay:
                    if (x == 'a'):
                        # Move left
                        mutations = -1
                    elif (x == 'd'):
                        # Move right
                        mutations = 1
                    elif (x == ''):
                        # Move forward
                        mutations = 0
                

                print("\033[H\033[J")
                i = i + 1

        if broken:
            lose_screen()
        if win:
            win_screen()

if __name__ == '__main__':
    ascii_racer()
