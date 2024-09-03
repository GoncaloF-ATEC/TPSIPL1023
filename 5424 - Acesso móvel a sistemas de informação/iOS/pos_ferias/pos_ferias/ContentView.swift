//
//  ContentView.swift
//  pos_ferias
//
//  Created by Gonçalo Feliciano on 03/09/2024.
//

import SwiftUI

struct ContentView: View {
    
    @StateObject var vm = APIHandler(url: "https://jsonplaceholder.typicode.com/todos")
    
    @State var id = 0;
    
    var body: some View {
        VStack {
            
            
            Text(vm.getTodo(id: id)?.title ?? "sem Info")
            Stepper("id: \(self.id)", value: self.$id)
            
        }//VStack
        .padding()
        .task {
            try! await vm.loadAllData()
        }
    }
}

#Preview {
    ContentView()
}
