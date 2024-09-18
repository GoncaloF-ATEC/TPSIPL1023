package pt.atec.a4_loadapi

import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path


interface APIHandler {

    //https://jsonplaceholder.typicode.com/comments
    @GET("comments")
    fun getCommnets(): Call<List<Comment>>

    //https://jsonplaceholder.typicode.com/comments/4
    @GET("comments/{id}")
    fun getCommnet(@Path("id") id: Int): Call<Comment>

}