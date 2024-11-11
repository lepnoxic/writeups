# Level 16: Terra Nova

## Problems

You cautiously step out of your damaged spaceship and breathe a sigh of relief having survived the tumultuous landing.
Having traversed a lengthy and arduous path, you ultimately set foot on Terra Nova, the planet for which you had done it all. You look around to find that you have not just explored a new planet but also...discovered extraterrestrial life. Before you lie a whole new civilisation, one whose likes you have never seen before. Crystalline structures that touch the sky but don’t seem to end, houses that each have a personality of their own, their architecture so advanced it defies all laws of physics. Floating gardens showcase a plethora of seasons, crystal clear lakes adorned with bioluminescent flowers, and majestic mountains bordering the far side of the planet. The view is unreal, it is a seamless blend of nature and technology. You are lost in your amazement when it hits you that even with such development around you, there seems to be no sign of life. Your curiosity piques and you start looking around for anything that could explain this situation. In your quest, you come across a magnificent building that leaves you awestruck. A dome-shaped structure that is so simple yet beautiful. Its smooth surface reflects the surrounding landscapes. The majestic dome rises into the sky, with captivating curves and a grand presence that evokes a sense of awe and wonder. You are certain that you will find your answers here but of course, the entrance is protected. You see multiple NUSB chips lying on the ground near the entrance. Desperate to find the flag you plug them into your lapdown decoder.
Reminder: Enclose the flag in sctf{}

## Writeup

We are given a folder with a .git folder, meaning we have to deal with git in some shape or manner. 

Checking .gitignore
```
linux@DESKTOP-565N39B:~/TerraNovaLaboratory$ cat .gitignore
...

# Important confidential lab files should stay local
*.txt

...
```

So there must be some text files that have been ignored.

git log and reflog

```
linux@DESKTOP-565N39B:~/TerraNovaLaboratory$ git log
commit 74e9812a9bf449dde8c1b073fe4b22e3912b1d9c (HEAD -> main)
Author: sibi361 <104310887+sibi361@users.noreply.github.com>
Date:   Fri Oct 6 21:09:40 2023 +0530

    Update gitignore

commit 09d7d987dbac3950639c3c88e92bb18066a63015 (origin/main, origin/HEAD)
Author: haqbilal <bilalhaq1219@outlook.com>
Date:   Tue Apr 12 14:24:00 2022 -0400

    wrote paper

commit 1f1c92f050376b991f60277d6f565d5948be9a37
Author: haqbilal <bilalhaq1219@outlook.com>
Date:   Tue Apr 12 11:25:05 2022 -0400

    updated gitignore

commit 0f033200c5c74d2d91f46f411b40a4d0ea4d0008
Author: haqbilal <bilalhaq1219@outlook.com>
Date:   Tue Apr 12 11:22:11 2022 -0400

    Added folder contents

commit 60590ce4d611d51debcc1f65ba56ec69c1d18451
Author: haqbilal <98703613+haqbilal@users.noreply.github.com>
Date:   Tue Apr 12 11:21:44 2022 -0400

    Update README.md
:
linux@DESKTOP-565N39B:~/TerraNovaLaboratory$ git reflog
74e9812 (HEAD -> main) HEAD@{0}: commit: Update gitignore
09d7d98 (origin/main, origin/HEAD) HEAD@{1}: reset: moving to HEAD^
0c83637 HEAD@{2}: commit: Shhhh
09d7d98 (origin/main, origin/HEAD) HEAD@{3}: checkout: moving from confid to main
3fc138f HEAD@{4}: commit: Shhhh
09d7d98 (origin/main, origin/HEAD) HEAD@{5}: checkout: moving from main to confid
09d7d98 (origin/main, origin/HEAD) HEAD@{6}: clone: from github.com:haqbilal/Evaluating-Claims-of-Extraterrestrial-Messaging.git
```

We have two interesting commits that we can check out. We can try to revert right before and onto them and check their diff to see anything that might be having the flag.

```
linux@DESKTOP-565N39B:~/TerraNovaLaboratory$ git diff 09d7d98 0c83637
diff --git a/.gitignore b/.gitignore
index bac7f1e..0f75979 100644
--- a/.gitignore
+++ b/.gitignore
@@ -15,6 +15,9 @@
 # User-specific files
 .Ruserdata

+# Important confidential lab files should stay local
+*.txt
+
 # Example code in package build process
 *-Ex.R

@@ -43,4 +46,4 @@ vignettes/*.pdf
 *.knit.md

 # R Environment Variables
-.Renviron
\ No newline at end of file
+.Renviron
```
```
linux@DESKTOP-565N39B:~/TerraNovaLaboratory$ git diff 09d7d98 3fc138f
diff --git a/top_secret_terra.txt b/top_secret_terra.txt
new file mode 100644
index 0000000..2502cc4
--- /dev/null
+++ b/top_secret_terra.txt
@@ -0,0 +1,5 @@
+"OG3w)r?zTGv_XASN);Cn)y{L%9/kb$qWcRd&..YbUfSwP;m/1(g$.s6i6gwQjZR?hz1+WCM.B`Q7m*lkdccN[R11T4tKOVojrX<.WrT;IbtEkgSjwdEQHi@m$@+9MBlBjc=v;qi?I^,BZgSA2mx=v1;;RFR,aPnGE)=r@8C"4%&DyTi%JQJH^3X8FJN{ZeLKuJgi`2Yv160oPyhdu!JM(6{L%30@^OnmMwxP,h5n79/.,`opo=Ca>RT2T4t1Z9jX:_1:Wk0lTet|j7R)c4G8?&Y>I,a4P5pto2f7=YCpL)/<PLmRBb:5+(*YKlx7m{omO2xAk~RAJfOA
+
+We the people of TerraNova believe in utmost throughput. Conquering the "91" galaxies by using the might one of the highest effeciency bases is what we are born to do.
+ZorbKillers
+
```
Alright now we can see a code and we see use of base and 91. Our best guess is the above code in encoded into base91. Decoding it we get

```
Terra Nova 2398 Laboratory

Lights
Main stage
Lab #1
Lab #2

Locks
Bastion Airlock v324 4343114
Inner Airlock v2 3924232
Dome Laboratory DoorLatch v24 PIN: d0mey_d0me_i_w0nt_forget_ojd32e2
Ratantan Poison Freezer Pin: 2328JKDqed2
Scavenging Anthill Model: cost %4232332

```

`sctf{d0mey_d0me_i_w0nt_forget_ojd32e2}`