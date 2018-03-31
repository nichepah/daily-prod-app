package com.example.pa.sailproduction;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.DatePicker;

public class XroadBSP extends AppCompatActivity implements DatePicker.OnDateChangedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xroad_bsp);

        DatePicker datePicker = findViewById(R.id.datePicker_bsp);
        datePicker.init(datePicker.getYear(), datePicker.getMonth(), datePicker.getDayOfMonth(), this);
    }

    /** Called when user taps GetLatest Button */
    public void getBSPData(View view) {
        final String a = "logcat";
        Log.d("getDSPData from XroadBSP", a);
        Intent intent = new Intent(this, DisplayDataBSP.class);
        startActivity(intent);
    }


    @Override
    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
        monthOfYear++;
        String myDate = String.valueOf(year)+"-"+String.valueOf(monthOfYear)+"-"+String.valueOf(dayOfMonth);
        Intent intent = new Intent(this, DateDisplayBSP.class);
        intent.putExtra("ProdDate", myDate);
        startActivity(intent);
    }
}
