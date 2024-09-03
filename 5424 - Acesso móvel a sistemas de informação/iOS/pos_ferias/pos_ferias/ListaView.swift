//
//  ListaView.swift
//  pos_ferias
//
//  Created by Gonçalo Feliciano on 03/09/2024.
//

import SwiftUI

struct ListaView: View {
    var listaTodos: TODOs
    var body: some View {
        List{
            
            ForEach(listaTodos) { todo in
                HStack{
                    
                    NavigationLink {
                        ToDoView(todo: todo)
                        
                        
                    } label: {
                        Text(todo.title)
                    }

                  
                    
                    
                }
                
                
            }
            
            
            
            
            
        }
    }
}

#Preview {
    ListaView(listaTodos: [])
}
