//
//  ContentView.swift
//  2_demo_ui_2
//
//  Created by Gonçalo Feliciano on 16/07/2024.
//


/*
 
 MVC
 
 */
import SwiftUI

struct ContentView: View {

    @StateObject var vm = ContentViewModel()
    // @ObservedObject var vm = ContentViewModel()   // <- verssões mais antigas
    
    
    var body: some View {
        VStack {
            
            Image(systemName: "person.crop.circle")
            Text(vm.nome)
            TextField(text: self.$vm.nomeTF) {
                HStack{
                    Text("nome: ")
                }
            }
            .frame(width: 200)
            .textFieldStyle(.roundedBorder)
            
            Button{
              //  vm.nomeTF = "Novo Nome 3"
                vm.mudarNome()
            }label: {
                /*@START_MENU_TOKEN@*/Text("Button")/*@END_MENU_TOKEN@*/
            }

        }
        .padding()
        .alert(isPresented: $vm.erro) {
          //Alert(title: Text("nome vazio"))
            Alert(title: Text("nome vazio"),
                  primaryButton: .default(Text("btn"), action: {
                self.vm.setName()
            }),
                  secondaryButton: .destructive(Text("Apagar"))
            
            )
        }
    }
}

#Preview {
    ContentView()
}
