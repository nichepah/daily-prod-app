package com.example.pa.sailproduction;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.DatePicker;

public class XroadASP extends AppCompatActivity implements DatePicker.OnDateChangedListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xroad_asp);

        DatePicker datePicker = findViewById(R.id.datePicker_asp);
        //int day = datePicker.getDayOfMonth();
        datePicker.init(datePicker.getYear(), datePicker.getMonth(), datePicker.getDayOfMonth(), this);

    }

    /** Called when user taps GetLatest Button */
    public void getASPData(View view) {
        final String a = "logcat";
        //Log.e("getDSPData from XroadASP", a);
        Intent intent = new Intent(this, DisplayDataASP.class);
        startActivity(intent);
    }

    @Override
    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
        //Toast.makeText(getApplicationContext(), String.valueOf(year), Toast.LENGTH_LONG).show();
        monthOfYear++;
        String myDate = String.valueOf(year)+"-"+String.valueOf(monthOfYear)+"-"+String.valueOf(dayOfMonth);
        Intent intent = new Intent(this, DateDisplayASP.class);
        intent.putExtra("ProdDate", myDate);
        Log.e("ASP Date from XroadASP", myDate);
        startActivity(intent);

    }
}
