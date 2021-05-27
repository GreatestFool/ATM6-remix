ARM6-remix is just a hackpack for a few friends and myself to play around with.

Please ignore.

---

## Changes

<details>
  <summary>Mod additions</summary>

  * [Mowzie's Mobs](https://www.curseforge.com/minecraft/mc-mods/mowzies-mobs)
      * ProjectID: 250498
      * fileID: 3271048
  * [Alex's Mobs](https://www.curseforge.com/minecraft/mc-mods/alexs-mobs)
      * ProjectID: 426558
      * fileID: 3308459
  * [Project: Vibrant Journeys](https://www.curseforge.com/minecraft/mc-mods/project-vibrant-journeys)
      * ProjectID: 300297
      * fileID: 3308560
  * [Effortless Building](https://www.curseforge.com/minecraft/mc-mods/effortless-building)
      * ProjectID: 302113
      * fileID: 3316956
  * [Nef's Medieval decoration](https://www.curseforge.com/minecraft/mc-mods/neoelfeos-medieval-pub-decoration)
      * ProjectID: 444384
      * fileID: 3296205
  * [Subterranean Wilderness](https://www.curseforge.com/minecraft/mc-mods/subterranean-wilderness)
      * ProjectID: 413426
      * fileID: 3299430
  * [Crossroads MC](https://www.curseforge.com/minecraft/mc-mods/crossroads-mc/)
      * ProjectID: 250231
      * fileID: 3246384
      * **Requires:** [Essentials](https://www.curseforge.com/minecraft/mc-mods/essentials)
        * ProjectID: 293752
        * fileID: 3319470
  * [Sophisticated Backpacks](https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks)
      * ProjectID: 422301
      * fileID: 3294628

</details>

<details>
  <summary>Mod removals</summary>

  Nothing here.

  Move along citizen.

</details>

---

## Potential changes

<details>
  <summary>Mod additions</summary>

  * Add [ItemZoom](https://www.curseforge.com/minecraft/mc-mods/itemzoom)
  * Add [Planttech 2](https://www.curseforge.com/minecraft/mc-mods/planttech-2)
    * NOTE Perhaps consider removing [Mystical Agriculture](https://www.curseforge.com/minecraft/mc-mods/mystical-agriculture)?

</details>

<details>
  <summary>Mod removals</summary>

  * Remove [Refined Storage](https://www.curseforge.com/minecraft/mc-mods/refined-storage)
    * Remove [RSInfinityBooster](https://www.curseforge.com/minecraft/mc-mods/rsinfinitybooster)
    * Remove [ExtraStorage](https://www.curseforge.com/minecraft/mc-mods/extrastorage)
    * Remove [Creative Wireless Transmitter](https://www.curseforge.com/minecraft/mc-mods/creative-wireless-transmitter)
    * Remove [Extra Disks](https://www.curseforge.com/minecraft/mc-mods/extra-disks)
    * Remove [Refined Storage Addons](https://www.curseforge.com/minecraft/mc-mods/refined-storage-addons)
  * Remove [RFTools Storage](https://www.curseforge.com/minecraft/mc-mods/rftools-storage)

</details>

<details>
  <summary>Other changes</summary>

  * Disable Industrial Foregoing's
    * Enchantment Extractor
    * Enchantment Applicator
    * Enchantment Factory
  * Fix Reliquary's Lilypad of Fertility recipe.
    * NOTE This currently has an [open issue here](https://github.com/AllTheMods/ATM-6/issues/1691).
  * ftbchunks-server
    * #Disables all land protection. Useful for private servers where everyone is trusted and claims are only used for forceloading.
    disable_protection = true
  * Disable: environmental tech
    * Lots of errors in the client about this and valkerylib (required lib)

</details>

---

## Configurations

### Modpack configuration

<details>
  <summary>manifest.json</summary>

  Append to the beginning of the file at its place.

  ```json
    "name": "All the Mods 6 : REMIX",
    "author": "ATMTeam : GreatestFool",
  ```

  Append one line before end of file.

  ```json
    "files": [
      {
        "projectID": 250498,
        "fileID": 3271048,
        "required": true
      },
      {
        "projectID": 426558,
        "fileID": 3308459,
        "required": true
      },
      {
        "projectID": 300297,
        "fileID": 3308560,
        "required": true
      },
      {
        "projectID": 302113,
        "fileID": 3316956,
        "required": true
      },
      {
        "projectID": 444384,
        "fileID": 3296205,
        "required": true
      },
      {
        "projectID": 413426,
        "fileID": 3299430,
        "required": true
      },
      {
        "projectID": 250231,
        "fileID": 3246384,
        "required": true
      },
      {
        "projectID": 293752,
        "fileID": 3319470,
        "required": true
      },
      {
        "projectID": 422301,
        "fileID": 3294628,
        "required": true
      }
    ],
  ```

</details>

<details>
  <summary>modlist.html</summary>

  Append one line before end of file.

  ```html
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/mowzies-mobs">Mowzie's Mobs (by bobmowzie)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/alexs-mobs">Alex's Mobs (by alex1the1666)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/project-vibrant-journeys">Project: Vibrant Journeys (by solis_nova123)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/effortless-building">Effortless Building (by Requioss)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/neoelfeos-medieval-pub-decoration">Nef's Medieval decoration (by neoelfe0)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/subterranean-wilderness">Subterranean Wilderness (by Melonslise)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/crossroads-mc">Crossroads MC (by Technomancer_isTaken)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/essentials">Essentials (by Technomancer_isTaken)</a></li>
  <li><a href="https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks">Sophisticated Backpacks (by P3pp3rF1y)</a></li>
  </ul>

  ```

</details>

---

### Mod configurations

<details>
  <summary>jei-client.toml</summary>

  ```toml
    #Display search bar in the center
    CenterSearch = true
  ```

</details>

<details>
  <summary>alexsmobs.toml</summary>

  ```toml
    #Whether mimicream can be used to duplicate items.
    mimicreamRepair = false
  ```

</details>

<details>
  <summary>crossroads-server.toml</summary>

  ```toml
  [Ores]
    #Generate Copper Ore?
    copper = false
    #Generate Tin Ore?
    tin = false
    #Generate Ruby Ore?
    ruby = false
  ```

</details>