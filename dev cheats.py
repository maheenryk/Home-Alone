#dev cheats

'shard-of-love', 'shard-of-patience', 'shard-of-strength', 'shard-of-bravery', 'shard-of-sacrifice'

# special attack 'ohdip'

#---------------- Player Stats ------------------------------
player_max = 600 #Maximum value the player can reach or obtain through heals and items
player_hp = 100 
defense_hp = 100 #"Shield" health. if below 0, shield hp = 0, you essentially can't use it.
defense_max = 100 #Shield Value you get after a fight

#------------------------------------------------------------
#--------------- Player Attack Options -----------------
player_attacks = ['punch', 'kick', 'scratch', 'defend'] #You can change this around or create an entirely new system!    
#------------------------------------------------------
kick_dmg = dice(20, 30)
punch_dmg = dice(10,20)
scratch_dmg = dice(5, 10)


#-------------------------  Enemy  ----------------------------------
enemy_hp = 100 #enemy set hp
enemy_max = 150
enemy_choice = ['Slash', 'Strike', 'Shriek', 'Shield'] #Choice.list that the enemy can choose from
slash_dmg = dice(20, 30)
strike_dmg = dice(10, 20)
shriek_dmg = dice(5, 10)                                                       
shield_hp = 70                                                     
#---------------------------------------------------------------------

#----------- Boss (Reflection of Yourself) ----------------
boss_hp = 300
boss_max = 600
boss_shield_hp = 300
boss_shield_max = 350
boss_slash_dmg = dice(40, 50)
boss_strike_dmg = dice(30, 40)
boss_shriek_dmg = dice(20, 30)