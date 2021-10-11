import { Component, OnInit } from '@angular/core';
import { Persona } from 'src/app/model/Persona';

@Component({
  selector: 'app-Persona',
  templateUrl: './Persona.component.html',
  styleUrls: ['./Persona.component.scss']
})
export class PersonaComponent implements OnInit {

  public data : Persona []=[
    {
      nombre : "Isaac",       
      apellido : "Gamboa",       
      direccion:"Calle 28 sur #9b - 73 este",    
      edad:"21",         
      telefono :"3123507952",      
      correo :"isok_gamboa@hotmail.com" 
    },
    {
      nombre : "Santiago",       
      apellido : "Roa",       
      direccion:"Calle 20  #5 - 1 ",    
      edad:"23",         
      telefono :"3134117981",      
      correo :"nelsonroa98@hotmail.com" 
    },
    {
      nombre : "Carlos",       
      apellido : "Hernandez",       
      direccion:"Calle 17  #4 - 53 ",    
      edad:"22",         
      telefono :"3124729500",      
      correo :"Doncarlos@hotmail.com" 
    }
  ]

  constructor() { }

  ngOnInit(): void {
  }

}