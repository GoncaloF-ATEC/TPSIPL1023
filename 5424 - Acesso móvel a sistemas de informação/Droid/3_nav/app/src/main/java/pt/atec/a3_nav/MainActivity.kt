package pt.atec.a3_nav

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import pt.atec.a3_nav.ui.theme._3_navTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {

            var navCtrl = rememberNavController()

            NavHost(navController = navCtrl,
                startDestination = "home", builder = {


                    composable("home"){
                        HomeActivity(navCtrl)
                    }

                    composable("info/{nome}/{nome2}",
                        arguments = listOf(navArgument("nome"){
                                type = NavType.StringType },
                            navArgument("nome2"){
                                type = NavType.StringType }
                    )

                    ){
                        val nome = it.arguments?.getString("nome") ?: "sem nome"
                        val foo = it.arguments?.getString("nome2") ?: "sem nome 2"
                        infoActivity(nome, foo)
                    }


                })



        }
    }
}