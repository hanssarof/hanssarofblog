---
title: 19 - Unsyncing ennemies animations on spawn
date: 2025-02-25
---
From the start, I had a problem with the snakes and their animations: they were all synchronized with each other. This made their movement very unnatural.

To remedy this, I decided to get around it with the simplest possible solution: add a small delay between each snake spawn. I divided the existant SpawnPoint SpawnActor function to make it more readable and now the loop adds a small random delay between every spawn.

<p style="text-align:center;"><img src="/images/New%20SpawnActor%20function.svg" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">Comparison of the two SpawnActor functions</p>
