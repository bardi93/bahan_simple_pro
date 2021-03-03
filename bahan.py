#=======Auto__Join=========
        if op.type in [13, 124]:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in owner or op.param2 in bot:
                        cl.acceptChatInvitation(op.param1)
            if c1mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in owner or op.param2 in bot:
                        c1.acceptChatInvitation(op.param1)
            if c2mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 in owner or op.param2 in bot:
                        c2.acceptChatInvitation(op.param1)
#=======Pro__Invite===========
        if op.type in [13, 124]:
            if op.param1 in protectinvite:
                if op.param2 not in creator or bot:
                    wait["blacklist"][op.param2] = True
                    for invite in op.param3.split('\x1e'):
                        if invite not in creator or bot:
                            wait["blacklist"][invite] = True
                            random.choice(botmid).cancelChatInvitation(op.param1, [invite])
                            random.choice(botmid).deleteOtherFromChat(op.param1, [op.param2])
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