//
//  ContentView.swift
//  Listas
//
//  Created by Gonçalo Feliciano on 23/07/2024.
//

import SwiftUI

struct ContentView: View {
    
    @StateObject var vm  = ContentViewModel()
    
    var body: some View {
        NavigationStack{
            VStack{
                HStack{
                    TextField("Novo nome", text: $vm.newName)
                        .textFieldStyle(.roundedBorder)
                        .frame(width: 200)
                    
                    Button{
                        self.vm.addNome()
                    } label: {
                        Text("Add Name")
                    }
                
                }
                
                List{
                    
                    ForEach(vm.startChar, id: \.self ){ char in
                        
                        if !vm.getContactosStarted(by: char).isEmpty{
                            Section{
                                ForEach(vm.getContactosStarted(by: char)){ ct in
                                    NavigationLink {
                                        Text(ct.nome)
                                    } label: {
                                        ListLineView(nome: ct.nome)
                                    }

                                    
                                   
                                    
                                }
                            }header: {
                                Text(char.uppercased())
                            }
                        }
                    }
                }
 
            }
            .listStyle(.insetGrouped)
            .onAppear(perform: {
                
               // vm.listaContactos.addDummyData()
                
                
            })
            .navigationTitle("Lista Contactos")
           
            
        }
        .alert(isPresented: $vm.showErroe) {
            Alert(title: Text("O nome não pode esta vazio"))
        }
        
        
        
    }
    
}

#Preview {
    ContentView()
}
