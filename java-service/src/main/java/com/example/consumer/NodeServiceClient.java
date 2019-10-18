package com.example.consumer;


import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * @author hejiabei
 * @date 2019/5/14 16:54
 */
@FeignClient("py-sidecar")
public interface NodeServiceClient {
    @GetMapping(value = "/execute")
    String execute(@RequestParam(value = "times")String times);
}
