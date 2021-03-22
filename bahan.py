Part 2
#=======Auto__Join=========
        if op.type in [13, 124]:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in botmid:
                        cl.acceptChatInvitation(op.param1)
            if c1mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in botmid:
                        c1.acceptChatInvitation(op.param1)
            if c2mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in creator or op.param2 in botmid:
                        c2.acceptChatInvitation(op.param1)
#=======Pro__Invite===========
        if op.type in [13, 124]:
            if op.param1 in proInvite:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    for invite in op.param3.split('\x1e'):
                        if invite not in creator or botmid:
                            wait["blacklist"][invite] = True
                            random.choice(bot).cancelChatInvitation(op.param1, [invite])
                            random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
#===========================
#Cmd proInvite

            if cmd == "proinvite on":
                if sender in creator:
                    if to not in proInvite:
                        proInvite.append(to)
                        cl.sendMessage(to, "pro invite aktif")
                    else:
                        cl.sendMessage(to, "pro invite sudah aktif")

            if cmd == "proinvite off":
                if sender in creator:
                    if to in proInvite:
                        proInvite.remove(to)
                        cl.sendMessage(to, "pro invite tidak aktif")
                    else:
                        cl.sendMessage(to, "pro invite sudah tidak aktif")
#============================================
 
 Part 3
#=======Protect______Kick=========
        if op.type in [19, 133, 32, 126]:
            if op.param1 in proKick:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                        random.choice(bot).findAndAddContactsByMid(op.param3)
                        random.choice(bot).inviteIntoChat(op.param1, [op.param3])
                    except:
                        pass
            if op.param1 in proCancel:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                        random.choice(bot).findAndAddContactsByMid(op.param3)
                        random.choice(bot).inviteIntoChat(op.param1, [op.param3])
                    except:
                        pass
            if op.param3 in creator and op.param3 in botmid:
                if op.param2 not in creator or botmid:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                        random.choice(bot).findAndAddContactsByMid(op.param3)
                        random.choice(bot).inviteIntoChat(op.param1, [op.param3])
                    except:
                        pass
#============================================
#Cmd protect kick

            if cmd == "prokick on":
                if sender in creator:
                    if to not in proKick:
                        proKick.append(to)
                        cl.sendMessage(to, "pro Kick aktif")
                    else:
                        cl.sendMessage(to, "pro Kick sudah aktif")

            if cmd == "prokick off":
                if sender in creator:
                    if to in proKick:
                        proKick.remove(to)
                        cl.sendMessage(to, "pro Kick tidak aktif")
                    else:
                        cl.sendMessage(to, "pro Kick sudah tidak aktif")
#Cmd protect cancel

            if cmd == "procancel on":
                if sender in creator:
                    if to not in proCancel:
                        proCancel.append(to)
                        cl.sendMessage(to, "pro Cancel aktif")
                    else:
                        cl.sendMessage(to, "pro Cancel sudah aktif")

            if cmd == "proinvite off":
                if sender in creator:
                    if to in proCancel:
                        proCancel.remove(to)
                        cl.sendMessage(to, "pro Cancel tidak aktif")
                    else:
                        cl.sendMessage(to, "pro Cancel sudah tidak aktif")
#============================================
Part 4
#pro qr
        if op.type in [11, 122]:
                if op.param1 in proQr:
                    if op.param2 not in creator or botmid:
                            if cl.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket == True:
                                try:
                                    wait["blacklist"][op.param2] = True
                                    random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                                    chat = random.choice(bot).getChats([op.param1])
                                    if chat.chats[0].extra.groupExtra.preventedJoinByTicket == True:
                                        random.choice(bot).updateChat(chat.chats[0],4)
                                    else:
                                        pass
                                except:
                                    pass
#projoin
        if op.type in [17, 130]:
                if op.param1 in proJoin:
                    if op.param2 not in creator or botmid:
                            random.choice(bot).deleteOtherFromChat(op.param1, [op.param2])
                                        
#Cmd protect url

            if cmd == "proqr on":
                if sender in creator:
                    if to not in proQr:
                        proQr.append(to)
                        cl.sendMessage(to, "pro url aktif")
                    else:
                        cl.sendMessage(to, "pro url sudah aktif")

            if cmd == "proqr off":
                if sender in creator:
                    if to in proQr:
                        proQr.remove(to)
                        cl.sendMessage(to, "pro url tidak aktif")
                    else:
                        cl.sendMessage(to, "pro url sudah tidak aktif")
#Cmd protect join

            if cmd == "projoin on":
                if sender in creator:
                    if to not in proJoin:
                        proJoin.append(to)
                        cl.sendMessage(to, "pro Join aktif")
                    else:
                        cl.sendMessage(to, "pro Join sudah aktif")

            if cmd == "projoin off":
                if sender in creator:
                    if to in proJoin:
                        proJoin.remove(to)
                        cl.sendMessage(to, "pro Join tidak aktif")
                    else:
                        cl.sendMessage(to, "pro Join sudah tidak aktif")





 