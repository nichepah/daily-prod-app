package com.example.pa.sailproduction;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.DatePicker;

public class XroadBSL extends AppCompatActivity implements DatePicker.OnDateChangedListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_xroad_bsl);

        DatePicker datePicker = findViewById(R.id.datePicker_bsl);
        datePicker.init(datePicker.getYear(), datePicker.getMonth(), datePicker.getDayOfMonth(), this);

    }

    /** Called when user taps getLatest button */
    public void getBSLData(View view) {
        final String a = "logcat";
        //Log.e("getDSPData from XroadASP", a);
        Intent intent = new Intent(this, DisplayDataBSL.class);
        startActivity(intent);
    }

    @Override
    public void onDateChanged(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
        //Toast.makeText(getApplicationContext(), String.valueOf(year), Toast.LENGTH_LONG).show();
        monthOfYear++;
        String myDate = String.valueOf(year)+"-"+String.valueOf(monthOfYear)+"-"+String.valueOf(dayOfMonth);
        Intent intent = new Intent(this, DateDisplayBSL.class);
        intent.putExtra("ProdDate", myDate);
        Log.e("BSL Date from XroadBSL", myDate);
        startActivity(intent);

    }
}
