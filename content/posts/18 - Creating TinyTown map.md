---
title: 18 - Creating TinyTown map
date: 2025-02-20
---
Until now, I had only a test map with a basic terrain so I decided to spend some on level design. I started by drafting a map of a small town blocked in a valley and blocked by a mountain.

My idea was to create a map with 3 attack paths for the snakes:
- One road from the north passing under a railway acting as a barrier for the player
- One canyon coming to the east
- One road coming from the west

!![Image Description](/images/Pasted%20image%2020250220142629.png)
<p style="text-align:center;">My wonderful drawing skills of a map: a first sketch</p>

After the drawing, I started in Blender. I thought that it will be quicker for me to sculpt the map and then export it to Unreal. To do so, I followed a video made by jimmyXR: [Level Up Your Landscapes in UE5 with Blender A.N.T. Landscapes](https://www.youtube.com/watch?v=-nHf90jt064). Is uses the A.N.T pluggin for blender to create the map and then import it as a height map in Unreal.

!![Image Description](/images/Pasted%20image%2020250220082923.png)
<p style="text-align:center;">My work in Blender using the A.N.T pluggin and the sculpting tools</p>

!![Image Description](/images/TinyTown.png)
<p style="text-align:center;">And the result as a height map</p>

Even if I am shure that the tutorial is good, I had an issue with the resolution and after importing it, the terrain was very blocky in Unreal. To fix that, I used the landscape brushes to smooth everything.

Also, the proportions in Blender were not as great as in the game. I take probably arount an hour to adjust the roads, the town terrain, the canyon and so on. After applying a basic color material, here is the final result:

!![Image Description](/images/Pasted%20image%2020250220083145.png)
<p style="text-align:center;">The result in Unreal</p>