plugins {
    id("com.android.library")
}

android {
    namespace = "com.example.login"
    compileSdk = 35
}

dependencies {
    implementation(project(":core:network"))
}
