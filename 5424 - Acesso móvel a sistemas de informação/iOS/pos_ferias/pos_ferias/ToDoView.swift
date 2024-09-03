//
//  ToDoView.swift
//  pos_ferias
//
//  Created by Gonçalo Feliciano on 03/09/2024.
//

import SwiftUI

struct ToDoView: View {
    
    var todo: TODO
    
    var body: some View {
        VStack{
            Text(todo.title)
                .font(.title)
            
            Text(todo.completed.description)
            
        }
    }
    
}

