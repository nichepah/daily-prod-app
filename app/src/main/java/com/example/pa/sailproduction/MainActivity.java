package com.example.pa.sailproduction;
/**
 * Author: Aneesh PA, DM, RDCIS
 * Written during
 * **/
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /** Called when user taps BSP Button */
    public void getXroadBSP(View view) {
        //final String a = "logcat";
        //Log.e("getBSPData", a);
        Intent intent = new Intent(this, XroadBSP.class);
        startActivity(intent);
    }

    /** Called when user taps DSP Button */
    public void getXroadDSP(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadDSP.class);
        startActivity(intent);
    }

    /** Called when user taps RSP Button */
    public void getXroadRSP(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadRSP.class);
        startActivity(intent);
    }

    /** Called when user taps BSL Button */
    public void getXroadBSL(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadBSL.class);
        startActivity(intent);
    }


    /** Called when user taps IISCO Button */
    public void getXroadIISCO(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadIISCO.class);
        startActivity(intent);
    }

    /** Called when user taps G5 Button */
    public void getXroadG5(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadG5.class);
        startActivity(intent);
    }

    /** Called when user taps SSP Button */
    public void getXroadSSP(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadSSP.class);
        startActivity(intent);
    }

    /** Called when user taps ASP Button */
    public void getXroadASP (View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadASP.class);
        startActivity(intent);
    }

    /** Called when user taps VISL Button */
    public void getXroadVISL(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadVISL.class);
        startActivity(intent);
    }

    /** Called when user taps SAIL Button */
    public void getXroadSAIL(View view) {
        //final String a = "logcat";
        //Log.e("getDSPData", a);
        Intent intent = new Intent(this, XroadSAIL.class);
        startActivity(intent);
    }


}
