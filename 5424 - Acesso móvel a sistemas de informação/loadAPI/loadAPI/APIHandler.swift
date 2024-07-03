//
//  APIHandler.swift
//  loadAPI
//
//  Created by Gonçalo Feliciano on 03/07/2024.
//

import Foundation


class APIHandler{
    
    var url: URL

    init(url: String) {
        self.url = URL(string: url)!
    }
    
    
    
    func loadAllPosts() async throws -> Posts{
        
        let urlReuquest = URLRequest(url: self.url)
        
        let (data, resp) = try await URLSession.shared.data(for: urlReuquest)
        
        guard let resp = resp as? HTTPURLResponse, (200...299).contains(resp.statusCode) else {
            
            throw myError.ErroResposta
        }
        
        let myData = try JSONDecoder().decode(Posts.self, from: data)
        
        
        return myData
    }
    


    func loadPostWith(id: Int) async throws -> Post{
        
        var url = url.appending(component: "\(id)")
        
        let urlReuquest = URLRequest(url: url)
        
        let (data, resp) = try await URLSession.shared.data(for: urlReuquest)
        
        guard let resp = resp as? HTTPURLResponse, (200...299).contains(resp.statusCode) else {
            
            throw myError.ErroResposta
        }
        
        let myData = try JSONDecoder().decode(Post.self, from: data)
        
        
        return myData

    }
        
}
