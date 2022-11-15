# SIGPE
Proyecto de ingeniería de software, sobre la gestión de proyectos extensionistas de las universidades

**Instalar el paquete psycopg2 para poder ejecutar migracones hacia la bd de postgres**
> ## Models
> Project
> * id
> * name 
> * area 
> * start_date
> * end_date
> * fundamentation
> * evaluation
> * conclution
> * recomendation

> Activities
> * id
> * activities_name
> * realization_date
> * descriptions
> * count_persons
> * Fk
>   * manager (Member)
>   * project


> Evidence
> * id
> * evidence_name
> * media
> * (ForeignKey)
>   * project

> Member
> * id
> * All default django user data 
> * ci
> * category
> * area
> * position
> * (Many to many)
>   * project
