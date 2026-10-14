package com.financial.portfolio.controller;


import com.financial.portfolio.model.Asset;
import com.financial.portfolio.service.AssetService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/assets")
public class AssetController {
    private final AssetService assetService;

    public AssetController(AssetService assetService) {
        this.assetService = assetService;
    }

    @PostMapping
    public ResponseEntity<Asset> createAsset(@Validated @RequestBody Asset asset)
    {
        Asset savedAsset = assetService.saveAsset(asset);
        return new ResponseEntity<>(savedAsset, HttpStatus.CREATED);
    }

    @GetMapping
    public  ResponseEntity<List<Asset>> getAllAssets()
    {
        List<Asset> assets = assetService.findAllAssets();
        return ResponseEntity.ok(assets);
    }

    @PostMapping("/batch")
    public List<Asset> createAssets(@RequestBody List<Asset> assets) {
        return assetService.saveAllAssets(assets);
    }
}
