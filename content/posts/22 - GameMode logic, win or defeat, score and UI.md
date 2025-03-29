---
title: 22 - GameMode logic, win or defeat, score and UI
date: 2025-03-14
---
After my detour through the weapon actions, I returned to the game loop logic. I started by creating a `DesertDefenderGameMode` class and used it for the TinyTown level. I added four functions:
- `ActivateSpawners()`, called from `PostLogin()`, to manage `SpawnPoints` and introduce a warmup delay before starting fight snakes.
- `PlayerEliminated()`, which sends the player back to the MainMenu map when he is killed by the snakes.
- `BasePointDestroyed()`, which sends the player back to the MainMenu map when the base is destroyed by the snakes.
- `PlayerWon()`, which sends the player back to the MainMenu map when he wins.

<p style="text-align:center;"><img src="/images/2025-03-15_19h03_16.png" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">SpawnPoints activated after a Warmup Delay</p>

Then, I created a `HUD` and `CharacterOverlay` classes to move the UI logic from level blueprints to C++. I parented my existing `WBP_Main` to the new class. I added a PlayerScore TextBlock in the top left corner of the screen and in the C++, I used the `UPROPERTY(meta = (BindWidget))` property to be able to modify the value from code.

<p style="text-align:center;"><img src="/images/2025-03-15_19h02_31.png" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">The WBP_Main parented to the CharacterOverlay with a PlayerScore TextBlock</p>

After that, I have setup all the UI related code in the `PlayerController` class to clean my code. Now, it is the controller that is responsible to call the HUD from `OnPosses()` to add the `WBP_Main` to the viewport, to initiate the score to 0 and to update the UI when snakes are killed .

<p style="text-align:center;"><img src="/images/2025-03-15_19h07_18.png" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">The WBP_Main PlayerScore updated after a kill</p>

Finally, I added a function in the `GameMode` so when the player score is higher than a value, the player wins the game.

In summary, now:
1. Snake is killed and calls `TakeDamage()`
2. The function calls `UpdatePlayerScore()` in the `PlayerController`
3. It updates the `PlayerScore` in the `CharacterOverlay` widget through the `HUD`
4. The `GameMode` checks win conditions
5. When the player or the base are attacked, the `GameMode` checks defeat conditions