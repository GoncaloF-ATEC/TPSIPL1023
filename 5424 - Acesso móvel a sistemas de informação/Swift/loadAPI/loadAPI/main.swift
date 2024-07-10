//
//  main.swift
//  loadAPI
//
//  Created by Gonçalo Feliciano on 03/07/2024.
//

import Foundation


let loader = APIHandler(url: "https://jsonplaceholder.typicode.com/posts")

//var myData = try await loader.loadAllPosts()


var myData = try await loader.loadPostWith(id: 3)
print(myData)


print("-------------")
myData = try await loader.loadPostWith(id: 8)
print(myData)
