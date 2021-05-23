ARM6-remix is just a hackpack for a few friends and myself to play around with.

Please ignore.

---

## Changes:

### Mod additions:
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
* [Sophisticated Backpacks](https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks)
    * ProjectID: 422301
    * fileID: 3294628

---

## Configuration snippets:

### manifest.json

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
      "projectID": 422301,
      "fileID": 3294628,
      "required": true
    }
  ],
```

### modlist.html

Append one line before end of file.

```html
<li><a href="https://www.curseforge.com/minecraft/mc-mods/mowzies-mobs">Mowzie's Mobs (by bobmowzie)</a></li>
<li><a href="https://www.curseforge.com/minecraft/mc-mods/alexs-mobs">Alex's Mobs (by alex1the1666)</a></li>
<li><a href="https://www.curseforge.com/minecraft/mc-mods/project-vibrant-journeys">Project: Vibrant Journeys (by solis_nova123)</a></li>
<li><a href="https://www.curseforge.com/minecraft/mc-mods/effortless-building">Effortless Building (by Requioss)</a></li>
<li><a href="https://www.curseforge.com/minecraft/mc-mods/neoelfeos-medieval-pub-decoration">Nef's Medieval decoration (by neoelfe0)</a></li>
<li><a href="https://www.curseforge.com/minecraft/mc-mods/subterranean-wilderness">Subterranean Wilderness (by Melonslise)</a></li>
<li><a href="https://www.curseforge.com/minecraft/mc-mods/crossroads-mc/">Crossroads MC (by Technomancer_isTaken)</a></li>
<li><a href="https://www.curseforge.com/minecraft/mc-mods/sophisticated-backpacks">Sophisticated Backpacks (by P3pp3rF1y)</a></li>
</ul>

```