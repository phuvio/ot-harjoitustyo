# Tehtävä 3 Sekvenssikaavio

```mermaid
 sequenceDiagram
   participant P as Main
   participant M as Machine
   participant F as FuelTank
   participant E as Engine
   P->>M: Machine()
   M->>F: FuelTank()
   M->>F: fill(40)
   M->>E: Engine(FuelTank())
   P->>M: drive()
   M->>E: start()
   E->>F: consume(5)
   E->>F: is_running()
   F-->E: 35
   E->>F: consume(10)
```
