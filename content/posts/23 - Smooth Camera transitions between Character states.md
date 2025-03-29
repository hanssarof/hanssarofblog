---
title: 23 - Smooth camera transitions between character states
date: 2025-03-16
---
Today I spend few hours to fix camera transitions. Previously, I have established three lengths for the character camera arm based on if the character is unequipped, equipped or equipped and aiming. I was changing those values in the `Equip` and `HideOrShowEquippedWeapon` functions of the `CombatComponent`. Also, I was just setting those values without transition resulting in a shaky gameplay.

To fix this, and to have my camera code in one place, I created a `InterpCameraArmLength` function using `FInterpTo` and `DeltaTime`. The function is called in the `TickComponent` an changes camera arm length continuously.

<p style="text-align:center;"><img src="/images/2025-03-18_13h52_46.png" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">The InterpCameraArmLength function called in TickComponent.</p>

For the moment, the function is still based on boolean combinations. In the future, I might use an enum to simplify how I handle character states. 

<p style="text-align:center;"><img src="/images/2025-03-18_14h04_49-ezgif.com-crop.gif" alt="Image Description"></p>
<p style="text-align:center; font-style:italic;">The smooth camera transition result (not so obvious in GIF format).</p>
