@startuml

(Solicitar login)
(Gerar XML) as (UC2)
Preferencias UC3
Contas a pagar (Last\nusecase) as UC4
Contas a receber (Last\nusecase) as UC4

:Sistema:
:Cliente: as Man2

left to right direction
package {
  actor Sistema as s
  actor "Cliente" as c
}
package {
  usecase "Solicitar login" as UC1
  usecase "Gerar XML" as UC2
  usecase "Preferências" as UC3
  usecase "Contas a pagar" as UC4
  usecase "Contas a receber" as UC5

}
s --> UC1
c --> UC2
c --> UC3
c --> UC4
c --> UC5


@enduml
