//
//  ContentView.swift
//  2_demo_ui_Nav
//
//  Created by Gonçalo Feliciano on 16/07/2024.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack{
        //NavigationView{ // <- mais antigos
            
            VStack {
                Image(systemName: "globe")
                    .imageScale(.large)
                    .foregroundStyle(.tint)
                Text("Hello, world!")
         
                Spacer().frame(height: 100)
                NavigationLink {
                    InfoView()
                } label: {
                    Text("Go to View 2")
                }

            }
            
            .navigationTitle("Home View")
            .navigationBarTitleDisplayMode(.large)
        
        
        }
        .padding()
        
        
        }
        
     
}

#Preview {
    ContentView()
}
