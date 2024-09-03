//
//  InfoView.swift
//  2_demo_ui_Nav
//
//  Created by Gonçalo Feliciano on 16/07/2024.
//

import SwiftUI

struct InfoView: View {
    var body: some View {
        NavigationStack{
            VStack{
                Image(systemName: "star.fill")
                    .foregroundStyle(.yellow)
                Text("View 2")
                
                NavigationLink {
                    Text("View 3")
                } label: {
                    Text("Go to View 3")
                }

            }
            .navigationTitle("Info View")
        }
    }
}
    

#Preview {
    InfoView()
}
