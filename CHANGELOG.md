# CHANGELOG

##  V0.13.1  🗓️ *2026-08-26*

### ✨ Novedades y Cambios Destacados

- **🚀 Naves y Vehículos:**
  - Nuevas naves: **Greycat Basher**, **Kruger S-65 Stingray** y **Gatac Tyilui**.
  - Variantes de misiones para **Drake Golem**, **Drake Clipper**, **ARGO Mole** y **MISC Prospector**.
  - Nuevas pinturas: esquemas temáticos y piratas para el Basher (*Razorburn*, *Corroded*, *Nightmare*, *Blue Blossom*), *SteelTek* y *Festival de la Base*.

- **📜 Misiones, Diálogos e Historia:**
  - **Levski & Alianza del Pueblo:** Más de 180 líneas para la cadena narrativa de *Recco Battaglia*, *Isaac* y el *Capitán Amir Lucas*.
  - **Asedio de Orison (SOO2):** Datapads, códigos y nuevos objetivos de evento.
  - **Foxwell & Cazadores de Recompensas:** Nuevos contratos contra oleadas de *XenoThreat* y ajustes en certificaciones BHG.

- **🏗️ Hangares, Carga y Terminales:**
  - **Ship Selector:** Opciones de reclamo y entrega de equipamiento/carga asegurada y predeterminada (*Snapshots*).
  - **Freight Elevators:** Mensajes de estado, inventario personal, avisos de sobrecarga y bloqueo de objetos robados o contenedores de misión.

- **⚔️ Equipamiento y Armas:**
  - Nuevas armas Greycat (*Deathroll Ballistic Gatling S2*, *Laser Repeater S2*).
  - Variantes de rifles Behring (*P4-AR Star Kitten*, *CQ7 Goldsmith/Snowfire/Infantry*) y armaduras pesadas *Morozov Stronghold*.

- **🧭 Interfaz (UI) y Calidad de Vida:**
  - Pistas y guías en pantalla para el acoplamiento y repostaje en vuelo (*Refueling*).
  - Notificaciones de disponibilidad de instancias en *mobiGlas*.
  - Correcciones ortográficas, acentuación y unificación de términos en todo el archivo.

##  v0.13.0  🗓️ *2026-07-16*

### ✨ Añadido
- **Misiones Northrock (Dubuisson)** — Diálogos completos del nuevo arco de misiones de Northrock Service Group
- **Arco Battaglia** — Diálogos, gestión de misión y UI de reputación de Recco Battaglia
- **Mendo Ren & Kepler** — Nuevos diálogos de PNJs
- **Sistema SOO2** — Objetivos, sub-objetivos, UI e introducción del sistema completo
- **Nuevas facciones** — Moraine / People's Alliance, Cornerstone Developments
- **Sistema Nyx** — Base Moraine, estación forajida, clúster de asteroides, tránsito
- **Nuevas naves y vehículos** — Drake, ARGO, MISC, ATLS (mecha), Golem, Fury, Salvation + series Apar y Behring
- **Sistema de Reabastecimiento** — UI completa, tipos de combustible (H2/Quantum/Ambos), mobiGlas CryAstro
- **Freight Elevator** — Reclamos, disponibilidad, obstrucciones, sobrecarga
- **Misiones genéricas** — BoardShip, ShipAmbuscade, DataDownload, CreateUplink, ORS (Construct, MedicalAid, BunkerRaid…)
- **UI diversa** — Ship Selector, notificaciones HUD, opciones de pausa, etiquetas de UI, scan de entidades+

### 🔄 Modificado
- Notificaciones de comercio entre jugadores actualizadas
- Strings de reabastecimiento UWC revisados
- Entrada general del diario actualizada
- Descripción de nave GATAC revisada

##  v0.12.5  🗓️ *2026-06-18*

* 2 naves añadidas con sus skins y componentes correspondientes: Gatac Railen y Gatac Tyilui
* Traducido los racks de bombas de la Eclipse, Retaliator y Gladiator
* Traducido notificación de solicitud de transferencia


##  v0.12.4  🗓️ *2026-06-05*

### 🛠️ Correcciones y Traducciones Clave
* **Respeto al Lore:** Se revirtieron traducciones literales a nombres oficiales de Star Citizen:
  * `Drake Blindado` ➡️ `Drake Ironclad`
  * `Asalto Blindado` ➡️ `Ironclad Asalto`
  * `Hoja Vanduul` ➡️ `Vanduul Blade`
* **Misiones de Bombardeo (Foxwell):** Traducidas del inglés al español las descripciones de las misiones `Foxwell_bombingrun_H/S/VE_desc_001`.
* **Interfaz de Control (HUD):**
  * `TARGET SELECTOR` ➡️ `SELECTOR DE OBJETIVO`
  * `TRGT. STATUS` ➡️ `ESTADO OBJ.`

### ➕ Nuevas Claves Destacadas
* **Diálogos de Combate (`PU_`):** `309` líneas de transmisiones de radio en español de la Alianza del Pueblo y combates con la fragata *Idris*.
* **Misión "Tranquility" (`Intersec_`):** `63` claves en español para asistir a la nave de la Alianza en Nyx.
* **Pinturas de la DefenseCon 2956 (`DefenseCon_`):** `48` descripciones de variantes estéticas (*125a Slate Camo*, *Asgard Sky Forge*, *Aurora MK2 Cloudbuster*, etc.).
* **Sistema de Repostaje (`refueling_`):** `45` claves de HUD e interfaces para la transferencia de combustible.
* **Otros:** `409` claves de equipamiento (`item_`), `38` de contratos de seguridad (`Foxwell_`) y `35` tipos de minerales minables (`mineabletype_`).

### 🗑️ Claves Depuradas (Eliminadas)
* **Limpieza de Sufijos:** Eliminación del sufijo redundante `,P` en claves de mensajería `FTLCourier_RepUI_*`.
* **Descripciones de Sistemas:** Remoción de textos obsoletos de localizaciones en *Pyro* y *Stanton*.
* **Configuraciones antiguas:** Retirada de parámetros de atenuación ESP en el menú de pausa y diálogos ambientales inactivos de *Hawker*.

---

##  v0.12.3  🗓️ *2026-05-13*

> 📋 Parche 4.8 Tactical Strike.
>
> **~500+ entradas traducidas** en total

### 🚀 Naves
8 naves nuevas: Aegis Tiburon, Origin M80, Drake Pitbull, MISC Starlite, Vanduul Mauler, Anvil Odin, Drake Command Module, Kruger L-22 Alpha Wolf; con sus respectivas skins

### 🔧 Mecánicas
- Sistema de **repostaje completo** (UI, pods, boquillas, misiones UWC, diálogos NPC)
- **Crafting**: 20+ componentes traducidos
- **Hangar**: desguace, seguro de carga, naves averiadas

### 🎯 Misiones
- **Tactical Strike Group (TSG)**: misión multi-fase en Sistema Nyx con diálogos completos
- **Defensa / XenoThreat**: contratos multi-nivel
- **Minería** con scanentities *(WIP)*

### 🛡️ Equipo
- 10+ armas FPS y armamento de la Vanduul Mauler
- 6 sets de armadura, trajes Tailwind, Flight Blades

### 🌍 Lore & UI
- Planetas/lunas de Pyro y Stanton, facciones (Shattered Blade, UWC), DefenseCon 2956

---

## v0.12.2 🗓️ *2026-04-11*

- Añadidas las líneas de la 4.7.1

---

## v0.12.1 🗓️ *2026-03-28*

### 🔄 Consistencia y Terminología

- **Unificación de GREMIO:** Se estandarizó el uso de `GREMIO` (en mayúsculas), eliminando variantes como `Gremio`, `GUILDA`, `GUILDE` y `Guild`.
- **Cazarrecompensas:** Ajustados roles y profesiones para mantener una capitalización consistente en diálogos y fichas de contrato.
- **Limpieza de "N/A":** Todas las instancias de `N / A` fueron corregidas a `N/A` para uniformidad en las entradas de reputación.

### 🐛 Correcciones de Formato (UI & Tags)

- **Action Tags:** Eliminados los espacios redundantes en etiquetas de acción (por ejemplo, `[~action(...) ]` ➜ `[~action(...)]`).
- **MobiGlas:** Corregido el espaciado en varias entradas de `Journal_General` para evitar saltos de línea no deseados.
- **Tutoriales:** Se añadió el prefijo `[N/A]` a los marcadores de misiones del tutorial, facilitando la depuración interna.
- **Terminología:** `Cazador de recompensas` ➜ `Cazarrecompensas`.

### 🧩 Otros Ajustes

- **Misiones (`~mission(Contractor)`):** Algunas descripciones fueron reescritas para evitar errores de reconocimiento debido a traducciones literales.
- Diversos **ajustes menores** de formato y coherencia interna.

---

## v0.12.0

- Pues que hay de nuevo viejo

---

## v0.11.3

- Cambiado `Atraque` por `Docking`
- Cambiado `llamaradas` por `bengalas` del sistema anti-misiles
- Centros de distribución (Habitaciones)
- Battle Arena (Lineas sueltas que estaban en inglés)
- Marine (Lineas sueltas que estaban en inglés)
- Sataball (Lineas sueltas que estaban en inglés)
- Líneas sueltas OEM de los fabricantes de naves que estaban en inglés
- Misión Data Dowload (Lineas  sueltas que estaban en inglés)

---

## v0.11.2
- Clovus Darnelli (Descripción de la Facción)
- Covalex (Misiones de la Facción)
- Castra (Descripciones)
- Lore Crusader (Personajes)
- Crusader Industries (Descripción de la Facción)
- Crsuader Security (Journal)

---

## v0.11.0
- Nuevos ATC (Servicios de aterrizaje)
- Advocacy Y ArCorp (Información de la Facción)
- Bit Zeroes (Misiones de la Facción)

---

## v0.10.3
- Se ha acortado la línea de `Cuidado del Paciente` a `Paciente` para que quepa en la bahía medica
