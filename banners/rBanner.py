import random

def random_banner():
    banner :str
    banners = ['''
 ____  __  __  ____  ____  ____  _  _ 
( ___)(  )(  )(_   )(_   )(  _ \( \/ )
 )__)  )(__)(  / /_  / /_  )___/ \  / 
(__)  (______)(____)(____)(__)   (__) 
''','''
  _____    _   _  _____   _____   ____   __   __ 
 |" ___|U |"|u| ||"_  /u |"_  /uU|  _"\ u\ \ / / 
U| |_  u \| |\| |U / //  U / // \| |_) |/ \ V /  
\|  _|/   | |_| |\/ /_   \/ /_   |  __/  U_|"|_u 
 |_|     <<\___/ /____|  /____|  |_|       |_|   
 )(\\,- (__) )(  _//<<,- _//<<,- ||>>_ .-,//|(_  
(__)(_/     (__)(__) (_/(__) (_/(__)__) \_) (__) 
''','''
 _______  __    __   ________   ________  .______   ____    ____ 
|   ____||  |  |  | |       /  |       /  |   _  \  \   \  /   / 
|  |__   |  |  |  | `---/  /   `---/  /   |  |_)  |  \   \/   /  
|   __|  |  |  |  |    /  /       /  /    |   ___/    \_    _/   
|  |     |  `--'  |   /  /----.  /  /----.|  |          |  |     
|__|      \______/   /________| /________|| _|          |__|     
                                                                 
''','''
 #######                      ######  #     # 
 #       #    # ###### ###### #     #  #   #  
 #       #    #     #      #  #     #   # #   
 #####   #    #    #      #   ######     #    
 #       #    #   #      #    #          #    
 #       #    #  #      #     #          #    
 #        ####  ###### ###### #          #    
                                              
''','''
 _______ _     _ ______ ______  _____  __   __
 |______ |     |  ____/  ____/ |_____]   \_/  
 |       |_____| /_____ /_____ |          |   
                                              
''','''
   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ 
 ( F | u | z | z | P | Y )
  \_/ \_/ \_/ \_/ \_/ \_/ 
''','''
8""""                   8""""8 8    8 
8     e   e eeeee eeeee 8    8 8    8 
8eeee 8   8 "   8 "   8 8eeee8 8eeee8 
88    8e  8 eeee8 eeee8 88       88   
88    88  8 88    88    88       88   
88    88ee8 88ee8 88ee8 88       88   
                                      
''','''
    ____                                ___   _  _ 
   F ___J  _    _    _____    _____    F _ ",FJ  LJ
  J |___: J |  | L  [__   F  [__   F  J `-' |J \/ F
  | _____|| |  | |  `-.'.'/  `-.'.'/  |  __/FJ\  /L
  F |____JF L__J J  .' (_(_  .' (_(_  F |__/  F  J 
 J__F    J\____,__LJ_______LJ_______LJ__|    |____|
 |__|     J____,__F|_______||_______||__L    |____|
                                                   
''','''
 (                   (          
 )\ )                )\ )       
(()/(    (          (()/( (     
 /(_))   )\  (   (   /(_)))\ )  
(_))_|_ ((_) )\  )\ (_)) (()/(  
| |_ | | | |((_)((_)| _ \ )(_)) 
| __|| |_| ||_ /|_ /|  _/| || | 
|_|   \___/ /__|/__||_|   \_, | 
                          |__/  
''','''
███████╗██╗   ██╗███████╗███████╗██████╗ ██╗   ██╗
██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔══██╗╚██╗ ██╔╝
█████╗  ██║   ██║  ███╔╝   ███╔╝ ██████╔╝ ╚████╔╝ 
██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔═══╝   ╚██╔╝  
██║     ╚██████╔╝███████╗███████╗██║        ██║   
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝        ╚═╝   
                                                  
''','''
  █████▒█    ██ ▒███████▒▒███████▒ ██▓███ ▓██   ██▓
▓██   ▒ ██  ▓██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░▓██░  ██▒▒██  ██▒
▒████ ░▓██  ▒██░░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ ▓██░ ██▓▒ ▒██ ██░
░▓█▒  ░▓▓█  ░██░  ▄▀▒   ░  ▄▀▒   ░▒██▄█▓▒ ▒ ░ ▐██▓░
░▒█░   ▒▒█████▓ ▒███████▒▒███████▒▒██▒ ░  ░ ░ ██▒▓░
 ▒ ░   ░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒▒▓▒░ ░  ░  ██▒▒▒ 
 ░     ░░▒░ ░ ░ ░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒░▒ ░     ▓██ ░▒░ 
 ░ ░    ░░░ ░ ░ ░ ░ ░ ░ ░░ ░ ░ ░ ░░░       ▒ ▒ ░░  
          ░       ░ ░      ░ ░             ░ ░     
                ░        ░                 ░ ░     
''','''
╔═╗╦ ╦┌─┐┌─┐╔═╗┬ ┬
╠╣ ║ ║┌─┘┌─┘╠═╝└┬┘
╚  ╚═╝└─┘└─┘╩   ┴ 
''','''
▄████ ▄   ▄▄▄▄▄▄   ▄▄▄▄▄▄   █ ▄▄ ▀▄    ▄ 
█▀   ▀ █ ▀   ▄▄▀  ▀   ▄▄▀   █   █  █  █  
█▀▀ █   █ ▄▀▀   ▄▀ ▄▀▀   ▄▀ █▀▀▀    ▀█   
█   █   █ ▀▀▀▀▀▀   ▀▀▀▀▀▀   █       █    
 █  █▄ ▄█                    █    ▄▀     
  ▀  ▀▀▀                      ▀          
                                         
''']
    banner = random.choice(banners)
    return banner

random_banner()