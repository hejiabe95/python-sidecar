package com.example.consumer;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by lenovo on 2017/12/16.
 */


@RestController
public class JavaController {

    @Autowired
    NodeServiceClient nodeServiceClient;

    @GetMapping(value = "/executeAlgorithm")
    public String sayHi(@RequestParam String times) {
        return nodeServiceClient.execute(times);
    }


}
