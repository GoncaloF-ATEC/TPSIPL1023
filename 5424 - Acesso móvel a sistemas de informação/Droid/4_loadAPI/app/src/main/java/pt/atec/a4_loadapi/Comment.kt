package pt.atec.a4_loadapi

import com.google.gson.annotations.SerializedName

/*
  {
    "postId": 1,
    "id": 1,
    "name": " txt ",
    "email": " txt ",
    "body": " txt "
  }

 */

class Comment (

    @SerializedName("postId")
    val postId: Int,

    @SerializedName("id")
    val id: Int,

    @SerializedName("name")
    val name: String,

    @SerializedName("email")
    val email: String,

    @SerializedName("body")
    val body:String
)